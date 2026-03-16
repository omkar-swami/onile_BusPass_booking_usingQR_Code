from flask import Blueprint, render_template, request
import pymysql
from pyzbar.pyzbar import decode
from PIL import Image
from datetime import datetime
import os

ScanQRCode = Blueprint("ScanQRCode", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )


@ScanQRCode.route('/ScanQRCode', methods=['GET','POST'])
def rScanQRCode_index():

    application_id = ""
    buspasslist = []
    img_Path = []
    applicatin_data = []
    status=""
    if request.method == "POST":

        file = request.files['qr_image']

        if file:

            path = os.path.join("static/uploads", file.filename)

            file.save(path)

            img = Image.open(path).convert("RGB")

            img = img.resize((800,800))

            result = decode(img)
            flag=0

            if result:
                for qr in result:
                    flag = 1
                    application_id = qr.data.decode("utf-8")  # correct attribute
            else:
                application_id = "QR Code Not Detected"

            if flag==1:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("""
                     SELECT 
                    pass_id,
                    pass_name,
                    full_name,
                    base_amount,
                    discount_amount,
                    final_amount,
                    issue_date,
                    expiry_date,
                    bus_pass.Status
                FROM bus_pass,
                     applications,
                     users,
                     pass_type
                WHERE bus_pass.application_id = applications.application_id
                AND applications.user_id = users.user_id
                AND bus_pass.pass_type_id = pass_type.pass_type_id
                AND bus_pass.application_id=%s
                     """,(application_id,))
                buspasslist = cursor.fetchall()
                expiry_date = buspasslist[0][7]

                expiry_date = datetime.strptime(str(expiry_date), "%Y-%m-%d")

                current_date = datetime.now()

                if current_date <= expiry_date:
                    status = "valid"
                else:
                    status = "expired"

                documentMaster=[]
                cursor.execute("""
                select * from documentsMaster where application_id =%s;
                """,(application_id,))
                documentMaster = cursor.fetchall()


                cursor.execute("""
                select * from documentDetails where document_id =%s
                and document_type_id=6
                """,(documentMaster[0][0],))
                documentdet = cursor.fetchall()
                img_Path = documentdet[0][3]


                cursor.execute("""
                select application_id,full_name,pass_name,
                route_source,route_destination,status,
                applied_date from applications,routes,
                users,pass_type 
                where applications.pass_type_id=pass_type.pass_type_id 
                and applications.route_id=routes.route_id 
                and applications.user_id=users.user_id
                and applications.application_id=%s
                """,(application_id,))
                applicatin_data = cursor.fetchall()

                pass
            
            os.remove(path)

    return render_template("/Search/ScanQRCode.html", buspasslist=buspasslist
                           ,img_Path=img_Path,applicatin_data=applicatin_data
                           ,status=status)