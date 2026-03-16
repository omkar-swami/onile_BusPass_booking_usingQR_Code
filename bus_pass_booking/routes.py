from flask import Blueprint, render_template, request
import pymysql

Routes = Blueprint("Routes", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewRouteID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(route_id) FROM routes")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


def clear_textbox():
    return '', '', '', '', ''


@Routes.route('/routes', methods=['GET', 'POST'])
def routes_index():

    routelist = []

    route_id = request.args.get('route_id', '')
    route_source = request.args.get('route_source', '')
    route_destination = request.args.get('route_destination', '')
    distance_km = request.args.get('distance_km', '')
    price_per_km = request.args.get('price_per_km', '')

    is_record = bool(route_id)

    if not is_record:
        route_id = GetNewRouteID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            route_id = request.form['route_id']
            route_source = request.form['route_source']
            route_destination = request.form['route_destination']
            distance_km = request.form['distance_km']
            price_per_km = request.form['price_per_km']

            if btn == 'Insert':
                cursor.execute("""
                    INSERT INTO routes 
                    VALUES (%s,%s,%s,%s,%s)
                """, (route_id, route_source, route_destination,
                      distance_km, price_per_km))
                conn.commit()

            elif btn == 'Update':
                cursor.execute("""
                    UPDATE routes 
                    SET route_source=%s,
                        route_destination=%s,
                        distance_km=%s,
                        price_per_km=%s
                    WHERE route_id=%s
                """, (route_source, route_destination,
                      distance_km, price_per_km, route_id))
                conn.commit()

            elif btn == 'Delete':
                cursor.execute("DELETE FROM routes WHERE route_id=%s", (route_id,))
                conn.commit()

            route_id, route_source, route_destination, distance_km, price_per_km = clear_textbox()
            route_id = GetNewRouteID()
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM routes")
    routelist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "routes.html",
        routelist=routelist,
        route_id=route_id,
        route_source=route_source,
        route_destination=route_destination,
        distance_km=distance_km,
        price_per_km=price_per_km,
        is_record=is_record
    )
