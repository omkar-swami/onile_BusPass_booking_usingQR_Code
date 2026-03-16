from flask import Blueprint, render_template, request
import pymysql

PassType = Blueprint("PassType", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewPassTypeID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(pass_type_id) FROM pass_type")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


def clear_textbox():
    return '', '', ''


@PassType.route('/pass_type', methods=['GET', 'POST'])
def pass_type_index():

    passtypelist = []

    pass_type_id = request.args.get('pass_type_id', '')
    pass_name = request.args.get('pass_name', '')
    validity_days = request.args.get('validity_days', '')

    is_record = bool(pass_type_id)

    if not is_record:
        pass_type_id = GetNewPassTypeID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            pass_type_id = request.form['pass_type_id']
            pass_name = request.form['pass_name']
            validity_days = request.form['validity_days']

            if btn == 'Insert':
                cursor.execute("""
                    INSERT INTO pass_type
                    VALUES (%s,%s,%s)
                """, (pass_type_id, pass_name, validity_days))
                conn.commit()

            elif btn == 'Update':
                cursor.execute("""
                    UPDATE pass_type
                    SET pass_name=%s,
                        validity_days=%s
                    WHERE pass_type_id=%s
                """, (pass_name, validity_days, pass_type_id))
                conn.commit()

            elif btn == 'Delete':
                cursor.execute("DELETE FROM pass_type WHERE pass_type_id=%s", (pass_type_id,))
                conn.commit()

            pass_type_id, pass_name, validity_days = clear_textbox()
            pass_type_id = GetNewPassTypeID()
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pass_type")
    passtypelist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "pass_type.html",
        passtypelist=passtypelist,
        pass_type_id=pass_type_id,
        pass_name=pass_name,
        validity_days=validity_days,
        is_record=is_record
    )
