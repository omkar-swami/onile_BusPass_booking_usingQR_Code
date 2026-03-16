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

UserLogIn = Blueprint("UserLogIn", __name__)

@UserLogIn.route('/UserLogIn', methods=['GET', 'POST'])
def UserLogIn_index():
    error = ""

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]
            session['userName'] = user[1]
            session['user_type_id'] = user[6]
            session["role"] = 'User'
            session["islogin"] = True

            return redirect(url_for("UserDashbaord.UserDashbaord_index"))
        else:
            error = "Invalid Email or Password"

    return render_template("UserLogIn.html", error=error)