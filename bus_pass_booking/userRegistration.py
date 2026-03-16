from flask import Blueprint, render_template, request, session,url_for,redirect
import pymysql
from datetime import datetime

userRegistration = Blueprint("userRegistration", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewUserID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(user_id) FROM users")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1
@userRegistration.route('/userRegistration', methods=['GET', 'POST'])
def userRegistration_index():


    usertypelist = []
    user_id = GetNewUserID()
    created_at = datetime.now().strftime('%Y-%m-%d')

    if request.method == 'POST':
        conn = connection()
        cursor = conn.cursor()

        try:
            user_id = request.form['user_id']
            full_name = request.form['full_name']
            email = request.form['email']
            mobile = request.form['mobile']
            password = request.form['password']
            address = request.form['address']
            user_type_id = request.form['user_type_id']
            created_at = request.form['created_at']
            cursor.execute("""
                    INSERT INTO users 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """, (user_id, full_name, email, mobile,
                      password, address, user_type_id, created_at))
            conn.commit()
            created_at = datetime.now().strftime('%Y-%m-%d')
            session['user_id'] = user_id
            session['userName'] =full_name
            session['user_type_id'] = user_type_id
            session["role"] = 'User'
            session["islogin"] = True
            return redirect(url_for("UserDashbaord.UserDashbaord_index"))

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()


    # Fetch user types for dropdown

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_type")
    usertypelist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "userRegistration.html",
        usertypelist=usertypelist,
        user_id=user_id,
        created_at=created_at,
    )
