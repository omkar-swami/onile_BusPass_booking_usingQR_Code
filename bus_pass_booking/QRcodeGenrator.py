from flask import Blueprint, render_template, request
import pymysql
import qrcode
import os

QRcodeGenrator = Blueprint("QRcodeGenrator", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

@QRcodeGenrator.route('/QRcodeGenrator', methods=['GET', 'POST'])
def QRcodeGenrator_index():

    application_id = request.args.get('application_id')
    file_nm = None

    if application_id:
        data = f"{application_id}"

        file_nm = f"application_Id_{application_id}.png"
        file_path = f"static/QRCodes/{file_nm}"

        # check if file already exists
        if not os.path.exists(file_path):
            # Create QR code object
            qr = qrcode.QRCode(
                version=3,  # small size
                box_size=15,  # size of each box
                border=4  # border around QR
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Make image with color
            img = qr.make_image(fill_color="black", back_color="white")

            # Save file
            img.save(file_path)

    return render_template("Search/QRcodeGenrator.html", file_nm=file_nm)