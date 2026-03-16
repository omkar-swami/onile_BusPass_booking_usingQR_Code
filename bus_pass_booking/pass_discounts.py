from flask import Blueprint, render_template, request
import pymysql

PassDiscounts = Blueprint("PassDiscounts", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewDiscountID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(discount_id) FROM pass_discounts")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


def clear_textbox():
    return '', '', '', ''


@PassDiscounts.route('/pass_discounts', methods=['GET', 'POST'])
def pass_discounts_index():

    discountlist = []
    usertypelist = []
    passtypelist = []

    discount_id = request.args.get('discount_id', '')
    user_type_id = request.args.get('user_type_id', '')
    pass_type_id = request.args.get('pass_type_id', '')
    discount_percentage = request.args.get('discount_percentage', '')

    is_record = bool(discount_id)

    if not is_record:
        discount_id = GetNewDiscountID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            discount_id = request.form['discount_id']
            user_type_id = request.form['user_type_id']
            pass_type_id = request.form['pass_type_id']
            discount_percentage = request.form['discount_percentage']

            if btn == 'Insert':
                cursor.execute("""
                    INSERT INTO pass_discounts
                    VALUES (%s,%s,%s,%s)
                """, (discount_id, user_type_id,
                      pass_type_id, discount_percentage))
                conn.commit()

            elif btn == 'Update':
                cursor.execute("""
                    UPDATE pass_discounts
                    SET user_type_id=%s,
                        pass_type_id=%s,
                        discount_percentage=%s
                    WHERE discount_id=%s
                """, (user_type_id, pass_type_id,
                      discount_percentage, discount_id))
                conn.commit()

            elif btn == 'Delete':
                cursor.execute("DELETE FROM pass_discounts WHERE discount_id=%s", (discount_id,))
                conn.commit()

            discount_id, user_type_id, pass_type_id, discount_percentage = clear_textbox()
            discount_id = GetNewDiscountID()
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    # Fetch dropdown data
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_type")
    usertypelist = cursor.fetchall()

    cursor.execute("SELECT * FROM pass_type")
    passtypelist = cursor.fetchall()

    # Fetch list with joins
    cursor.execute("""
        SELECT * FROM pass_discounts """)
    discountlist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "pass_discounts.html",
        discountlist=discountlist,
        usertypelist=usertypelist,
        passtypelist=passtypelist,
        discount_id=discount_id,
        user_type_id=user_type_id,
        pass_type_id=pass_type_id,
        discount_percentage=discount_percentage,
        is_record=is_record
    )
