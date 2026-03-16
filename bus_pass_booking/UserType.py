from flask import Blueprint, render_template, request
import pymysql

UserType = Blueprint("UserType", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewUserTypeID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(user_type_id) FROM user_type")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


def clear_textbox():
    return '', ''


@UserType.route('/user_type', methods=['GET', 'POST'])
def user_type_index():

    usertypelist = []
    user_type_id = request.args.get('user_type_id', '')
    type_name = request.args.get('type_name', '')
    is_record = bool(user_type_id)

    if not is_record:
        user_type_id = GetNewUserTypeID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            user_type_id = request.form['user_type_id']
            type_name = request.form['type_name']

            if btn == 'Insert':
                cursor.execute(
                    "INSERT INTO user_type VALUES (%s,%s)",
                    (user_type_id, type_name)
                )
                conn.commit()
                user_type_id, type_name = clear_textbox()
                user_type_id = GetNewUserTypeID()
                is_record = False

            elif btn == 'Update':
                cursor.execute(
                    "UPDATE user_type SET type_name=%s WHERE user_type_id=%s",
                    (type_name, user_type_id)
                )
                conn.commit()
                user_type_id, type_name = clear_textbox()
                user_type_id = GetNewUserTypeID()
                is_record = False

            elif btn == 'Delete':
                cursor.execute(
                    "DELETE FROM user_type WHERE user_type_id=%s",
                    (user_type_id,)
                )
                conn.commit()
                user_type_id, type_name = clear_textbox()
                user_type_id = GetNewUserTypeID()
                is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_type")
    usertypelist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "user_type.html",
        usertypelist=usertypelist,
        user_type_id=user_type_id,
        type_name=type_name,
        is_record=is_record
    )
