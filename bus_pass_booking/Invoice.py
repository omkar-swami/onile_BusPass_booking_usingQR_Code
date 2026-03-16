from flask import Blueprint, render_template, request, session
import pymysql

Invoice = Blueprint("Invoice", __name__)


def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )


@Invoice.route('/Invoice', methods=['GET', 'POST'])
def Invoice_index():
    inoive_data = []
    user_data=[]
    if request.method == 'GET':
        pass_id = request.args.get('pass_id')
        user_id=0
        if 'user_id' in session:
            user_id=session['user_id']


        conn = connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT pass_id, pass_name, bus_pass.application_id, full_name,
                   base_amount, discount_amount, final_amount, issue_date, expiry_date,
                   route_source, route_destination, payment_date
            FROM bus_pass, pass_type, applications, users, routes, payments
            WHERE bus_pass.pass_type_id = pass_type.pass_type_id
              AND bus_pass.application_id = applications.application_id
              AND applications.user_id = users.user_id
              AND applications.route_id = routes.route_id
              AND bus_pass.application_id = payments.application_id
              AND bus_pass.pass_id = %s
        """, (pass_id,))

        inoive_data = cursor.fetchall()
        cursor.execute("select * from users where user_id = '%s'" % user_id)
        user_data = cursor.fetchall()

        cursor.close()
        conn.close()

    return render_template(
        "Search/Invoice.html",
        inoive_data=inoive_data,
        user_data=user_data,
    )