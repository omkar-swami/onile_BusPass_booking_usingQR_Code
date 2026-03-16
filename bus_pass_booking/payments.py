from flask import Blueprint, render_template, request
import pymysql

Payments = Blueprint("Payments", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewPaymentID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(payment_id) FROM payments")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


@Payments.route('/payments', methods=['GET', 'POST'])
def payments_index():

    paymentlist = []
    applicationlist = []

    payment_id = request.args.get('payment_id', '')
    application_id = request.args.get('application_id', '')
    amount = request.args.get('amount', '')
    payment_date = request.args.get('payment_date', '')

    is_record = bool(payment_id)

    if not is_record:
        payment_id = GetNewPaymentID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            payment_id = request.form['payment_id']
            application_id = request.form['application_id']
            amount = request.form['amount']
            payment_date = request.form['payment_date']

            if btn == 'Insert':
                cursor.execute(
                    "INSERT INTO payments VALUES (%s,%s,%s,%s)",
                    (payment_id, application_id, amount, payment_date)
                )
                conn.commit()

            elif btn == 'Update':
                cursor.execute(
                    "UPDATE payments SET application_id=%s, amount=%s, payment_date=%s WHERE payment_id=%s",
                    (application_id, amount, payment_date, payment_id)
                )
                conn.commit()

            elif btn == 'Delete':
                cursor.execute(
                    "DELETE FROM payments WHERE payment_id=%s",
                    (payment_id,)
                )
                conn.commit()

            payment_id = GetNewPaymentID()
            application_id = ''
            amount = ''
            payment_date = ''
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()

    # Dropdown
    cursor.execute("SELECT application_id FROM applications")
    applicationlist = cursor.fetchall()

    # Table display (NO JOIN)
    cursor.execute("SELECT * FROM payments")
    paymentlist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "payments.html",
        paymentlist=paymentlist,
        applicationlist=applicationlist,
        payment_id=payment_id,
        application_id=application_id,
        amount=amount,
        payment_date=payment_date,
        is_record=is_record
    )
