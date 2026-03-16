from flask import Blueprint, render_template, request
import pymysql
import qrcode
import os

ApplicationRequest = Blueprint("ApplicationRequest", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

@ApplicationRequest.route('/ApplicationRequest', methods=['GET', 'POST'])
def ApplicationRequest_index():
    applicationlist=[]
    conn = connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        btn=request.form.get("btn")
        if btn=="Approved":
            application_id=request.form.get("application_id")
            cursor.execute("update applications set status='Approved' where application_id=%s ", (application_id,))
            cursor.execute("update bus_pass set Status ='Approved' where application_id=%s ", (application_id,))
            conn.commit()
        elif btn=="Rejected":
            application_id = request.form.get("application_id")
            cursor.execute("update applications set status='Rejected' where application_id=%s ", (application_id,))
            cursor.execute("update bus_pass set Status ='Rejected' where application_id=%s ", (application_id,))
            conn.commit()
    cursor.execute(
        """select application_id,full_name,pass_name,route_source,route_destination
        ,status,applied_date from applications,routes,users,pass_type 
        where applications.pass_type_id=pass_type.pass_type_id 
        and applications.route_id=routes.route_id 
        and applications.user_id=users.user_id
         order by applications.application_id ;""")
    applicationlist = cursor.fetchall()
    return render_template(
        "Search/ApplicationRequest.html",
        applicationlist=applicationlist
    )