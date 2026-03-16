from flask import Blueprint, render_template, request, session, redirect, url_for
import pymysql

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

UsersPassApplications = Blueprint("UsersPassApplications", __name__)
@UsersPassApplications.route('/UsersPassApplications', methods=['GET', 'POST'])
def UsersPassApplications_index():
    applicationlist=[]
    conn = connection()
    cursor = conn.cursor()
    user_id=0
    if 'user_id' in session:
        user_id=session['user_id']
    cursor.execute(
        """select application_id,full_name,pass_name,
        route_source,route_destination,status,applied_date 
        from applications,routes,users,pass_type
         where applications.pass_type_id=pass_type.pass_type_id
          and applications.route_id=routes.route_id 
          and applications.user_id=users.user_id
          and applications.user_id=%s;""",(user_id,))
    applicationlist = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template(
        "Search/UsersPassApplications.html",
        applicationlist=applicationlist
    )