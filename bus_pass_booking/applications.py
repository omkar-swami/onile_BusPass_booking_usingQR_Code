from flask import Blueprint, render_template, request
import pymysql
from datetime import datetime

Applications = Blueprint("Applications", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewApplicationID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(application_id) FROM applications")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


def clear_textbox():
    return '', '', '', '', '', ''


@Applications.route('/applications', methods=['GET', 'POST'])
def applications_index():

    applicationlist = []
    userlist = []
    passtypelist = []
    routelist = []

    application_id = request.args.get('application_id', '')
    user_id = request.args.get('user_id', '')
    pass_type_id = request.args.get('pass_type_id', '')
    route_id = request.args.get('route_id', '')
    status = request.args.get('status', '')
    applied_date = request.args.get('applied_date', '')

    is_record = bool(application_id)

    if not is_record:
        application_id = GetNewApplicationID()
        applied_date = datetime.now().strftime('%Y-%m-%d')

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            application_id = request.form['application_id']
            user_id = request.form['user_id']
            pass_type_id = request.form['pass_type_id']
            route_id = request.form['route_id']
            status = request.form['status']
            applied_date = request.form['applied_date']

            if btn == 'Insert':
                cursor.execute("""
                    INSERT INTO applications
                    VALUES (%s,%s,%s,%s,%s,%s)
                """, (application_id, user_id,
                      pass_type_id, route_id,
                      status, applied_date))
                conn.commit()

            elif btn == 'Update':
                cursor.execute("""
                    UPDATE applications
                    SET user_id=%s,
                        pass_type_id=%s,
                        route_id=%s,
                        status=%s,
                        applied_date=%s
                    WHERE application_id=%s
                """, (user_id, pass_type_id,
                      route_id, status,
                      applied_date, application_id))
                conn.commit()

            elif btn == 'Delete':
                cursor.execute("DELETE FROM applications WHERE application_id=%s", (application_id,))
                conn.commit()

            application_id, user_id, pass_type_id, route_id, status, applied_date = clear_textbox()
            application_id = GetNewApplicationID()
            applied_date = datetime.now().strftime('%Y-%m-%d')
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    # Fetch dropdown data
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_id, full_name FROM users")
    userlist = cursor.fetchall()

    cursor.execute("SELECT pass_type_id, pass_name FROM pass_type")
    passtypelist = cursor.fetchall()

    cursor.execute("SELECT route_id, route_source, route_destination FROM routes")
    routelist = cursor.fetchall()

    # Fetch application list with joins
    cursor.execute("""
        SELECT *
        FROM applications
    """)
    applicationlist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "applications.html",
        applicationlist=applicationlist,
        userlist=userlist,
        passtypelist=passtypelist,
        routelist=routelist,
        application_id=application_id,
        user_id=user_id,
        pass_type_id=pass_type_id,
        route_id=route_id,
        status=status,
        applied_date=applied_date,
        is_record=is_record
    )
