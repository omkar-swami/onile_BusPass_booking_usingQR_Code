from flask import Blueprint, render_template, request, session
import pymysql
def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

UserDashbaord = Blueprint("UserDashbaord", __name__)
@UserDashbaord.route('/UserDashbaord', methods=['GET', 'POST'])
def UserDashbaord_index():
    UserName = ""
    if 'userName' in session:
        UserName = session.get('userName')

    return render_template("UserDashbaord.html",UserName=UserName)