from flask import Blueprint, render_template, request
import pymysql

BusPass = Blueprint("BusPass", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewPassID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(pass_id) FROM bus_pass")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


@BusPass.route('/bus_pass', methods=['GET', 'POST'])
def bus_pass_index():

    buspasslist = []
    passtypelist = []
    applicationlist = []

    pass_id = request.args.get('pass_id', '')
    pass_type_id = request.args.get('pass_type_id', '')
    application_id = request.args.get('application_id', '')
    base_amount = request.args.get('base_amount', '')
    discount_amount = request.args.get('discount_amount', '')
    final_amount = request.args.get('final_amount', '')
    issue_date = request.args.get('issue_date', '')
    expiry_date = request.args.get('expiry_date', '')
    status=request.args.get('status', '')

    is_record = bool(pass_id)

    if not is_record:
        pass_id = GetNewPassID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            pass_id = request.form['pass_id']
            pass_type_id = request.form['pass_type_id']
            application_id = request.form['application_id']
            base_amount = request.form['base_amount']
            discount_amount = request.form['discount_amount']
            final_amount = request.form['final_amount']
            issue_date = request.form['issue_date']
            expiry_date = request.form['expiry_date']
            status=request.form['status']

            if btn == 'Insert':
                cursor.execute(
                    "INSERT INTO bus_pass VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (pass_id, pass_type_id, application_id,
                     base_amount, discount_amount,
                     final_amount, issue_date, expiry_date,status)
                )
                conn.commit()

            elif btn == 'Update':
                cursor.execute(
                    """UPDATE bus_pass 
                       SET pass_type_id=%s, application_id=%s,
                           base_amount=%s, discount_amount=%s,
                           final_amount=%s, issue_date=%s,
                           expiry_date=%s, status=%s
                       WHERE pass_id=%s""",
                    (pass_type_id, application_id,
                     base_amount, discount_amount,
                     final_amount, issue_date,
                     expiry_date, status,
                     pass_id)
                )
                conn.commit()

            elif btn == 'Delete':
                cursor.execute(
                    "DELETE FROM bus_pass WHERE pass_id=%s",
                    (pass_id,)
                )
                conn.commit()

            pass_id = GetNewPassID()
            pass_type_id = ''
            application_id = ''
            base_amount = ''
            discount_amount = ''
            final_amount = ''
            issue_date = ''
            expiry_date = ''
            status=''
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pass_type")
    passtypelist = cursor.fetchall()

    cursor.execute("SELECT * FROM applications")
    applicationlist = cursor.fetchall()

    cursor.execute("SELECT * FROM bus_pass")
    buspasslist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "bus_pass.html",
        buspasslist=buspasslist,
        passtypelist=passtypelist,
        applicationlist=applicationlist,
        pass_id=pass_id,
        pass_type_id=pass_type_id,
        application_id=application_id,
        base_amount=base_amount,
        discount_amount=discount_amount,
        final_amount=final_amount,
        issue_date=issue_date,
        expiry_date=expiry_date,
        status=status,
        is_record=is_record
    )
