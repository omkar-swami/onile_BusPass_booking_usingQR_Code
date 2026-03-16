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

SearchAllRoutes = Blueprint("SearchAllRoutes", __name__)
@SearchAllRoutes.route('/SearchAllRoutes', methods=['GET', 'POST'])
def UserDashbaord_index():
    routelist=[]
    route_sourcelist=[]
    route_destinationlist=[]
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']
        if source!="None" and destination!="None":
            cursor.execute("SELECT * FROM routes where route_source=%s AND route_destination=%s",(source,destination))
        elif source!="None" and destination=="None":
            cursor.execute("SELECT * FROM routes where route_source=%s", (source))
        elif source=="None" and destination!="None":
            cursor.execute("SELECT * FROM routes where route_destination=%s", ( destination))
        else:
            cursor.execute("SELECT * FROM routes")
    if request.method == 'GET':
        cursor.execute("SELECT * FROM routes")
    routelist = cursor.fetchall()
    cursor.execute("SELECT DISTINCT  route_source  FROM routes")
    route_sourcelist=cursor.fetchall()
    cursor.execute("SELECT DISTINCT  route_destination  FROM routes")
    route_destinationlist = cursor.fetchall()

    return render_template("Search/SearchAllRoutes.html",routelist=routelist,route_sourcelist=route_sourcelist,route_destinationlist=route_destinationlist,)