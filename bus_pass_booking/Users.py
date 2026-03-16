from flask import Blueprint, render_template, request
import pymysql
from datetime import datetime

Users = Blueprint("Users", __name__)

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


def clear_textbox():
    return '', '', '', '', '', '', '', ''


@Users.route('/users', methods=['GET', 'POST'])
def users_index():

    userlist = []
    usertypelist = []

    user_id = request.args.get('user_id', '')
    full_name = request.args.get('full_name', '')
    email = request.args.get('email', '')
    mobile = request.args.get('mobile', '')
    password = request.args.get('password', '')
    address = request.args.get('address', '')
    user_type_id = request.args.get('user_type_id', '')
    created_at = request.args.get('created_at', '')

    is_record = bool(user_id)

    if not is_record:
        user_id = GetNewUserID()
        created_at = datetime.now().strftime('%Y-%m-%d')

    if request.method == 'POST':
        btn = request.form['btn']
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

            if btn == 'Insert':
                cursor.execute("""
                    INSERT INTO users 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """, (user_id, full_name, email, mobile,
                      password, address, user_type_id, created_at))
                conn.commit()

            elif btn == 'Update':
                cursor.execute("""
                    UPDATE users 
                    SET full_name=%s, email=%s, mobile=%s,
                        password=%s, address=%s,
                        user_type_id=%s, created_at=%s
                    WHERE user_id=%s
                """, (full_name, email, mobile, password,
                      address, user_type_id, created_at, user_id))
                conn.commit()

            elif btn == 'Delete':
                cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
                conn.commit()

            user_id, full_name, email, mobile, password, address, user_type_id, created_at = clear_textbox()
            user_id = GetNewUserID()
            created_at = datetime.now().strftime('%Y-%m-%d')
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    # Fetch users
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    select * from users
    """)
    userlist = cursor.fetchall()

    # Fetch user types for dropdown
    cursor.execute("SELECT * FROM user_type")
    usertypelist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "users.html",
        userlist=userlist,
        usertypelist=usertypelist,
        user_id=user_id,
        full_name=full_name,
        email=email,
        mobile=mobile,
        password=password,
        address=address,
        user_type_id=user_type_id,
        created_at=created_at,
        is_record=is_record
    )
