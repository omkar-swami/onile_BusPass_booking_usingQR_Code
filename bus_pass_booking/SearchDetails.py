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

SearchDetails = Blueprint("SearchDetails", __name__)
@SearchDetails.route('/SearchDetails', methods=['GET', 'POST'])
def SearchDetails_index():
        passDetlist=[]
        routedata=[]
        conn = connection()
        cursor = conn.cursor()
        if request.method == 'GET':
            route_id=request.args.get('route_id')
            cursor.execute("SELECT * FROM routes where route_id=%s", (route_id,))
            routedata=cursor.fetchall()
            user_type_id=0
            if "user_type_id" in session:
                user_type_id=session['user_type_id']
                cursor.execute(""" 
                            select discount_id,type_name,pass_name,validity_days,
                            discount_percentage ,pass_discounts.user_type_id,pass_discounts.pass_type_id 
                            from pass_discounts,pass_type,user_type 
                            where pass_discounts.user_type_id=user_type.user_type_id 
                            and pass_discounts.pass_type_id = pass_type.pass_type_id 
                            and pass_discounts.user_type_id=%s
                            order by type_name;
                            """, (user_type_id,))
            else:
                cursor.execute(""" 
                            select discount_id,type_name,pass_name,validity_days,
                            discount_percentage ,pass_discounts.user_type_id,pass_discounts.pass_type_id 
                            from pass_discounts,pass_type,user_type 
                            where pass_discounts.user_type_id=user_type.user_type_id 
                            and pass_discounts.pass_type_id = pass_type.pass_type_id 
                            order by type_name;
                            """)


            passDetlist=cursor.fetchall()


        return render_template("Search/SearchDetails.html",route_id=route_id,passDetlist=passDetlist,routedata=routedata,user_type_id=user_type_id )
