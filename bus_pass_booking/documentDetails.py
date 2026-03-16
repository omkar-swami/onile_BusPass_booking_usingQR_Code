from flask import Blueprint, render_template, request
import pymysql

DocumentDetails = Blueprint("DocumentDetails", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewDocumentDetID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(documentDet_id) FROM documentDetails")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


@DocumentDetails.route('/documentDetails', methods=['GET', 'POST'])
def document_details_index():

    documentdetailslist = []
    documentlist = []
    documenttypelist = []

    documentDet_id = request.args.get('documentDet_id', '')
    document_id = request.args.get('document_id', '')
    document_type_id = request.args.get('document_type_id', '')
    photo = request.args.get('photo', '')

    is_record = bool(documentDet_id)

    if not is_record:
        documentDet_id = GetNewDocumentDetID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            documentDet_id = request.form['documentDet_id']
            document_id = request.form['document_id']
            document_type_id = request.form['document_type_id']
            photo = request.form['photo']

            if btn == 'Insert':
                cursor.execute(
                    "INSERT INTO documentDetails VALUES (%s,%s,%s,%s)",
                    (documentDet_id, document_id, document_type_id, photo)
                )
                conn.commit()

            elif btn == 'Update':
                cursor.execute(
                    "UPDATE documentDetails SET document_id=%s, document_type_id=%s, photo=%s WHERE documentDet_id=%s",
                    (document_id, document_type_id, photo, documentDet_id)
                )
                conn.commit()

            elif btn == 'Delete':
                cursor.execute(
                    "DELETE FROM documentDetails WHERE documentDet_id=%s",
                    (documentDet_id,)
                )
                conn.commit()

            documentDet_id = GetNewDocumentDetID()
            document_id = ''
            document_type_id = ''
            photo = ''
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()

    # Dropdowns
    cursor.execute("SELECT * FROM documentsMaster")
    documentlist = cursor.fetchall()

    cursor.execute("SELECT * FROM document_types")
    documenttypelist = cursor.fetchall()

    # Table display (NO JOIN)
    cursor.execute("SELECT * FROM documentDetails")
    documentdetailslist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "documentDetails.html",
        documentdetailslist=documentdetailslist,
        documentlist=documentlist,
        documenttypelist=documenttypelist,
        documentDet_id=documentDet_id,
        document_id=document_id,
        document_type_id=document_type_id,
        photo=photo,
        is_record=is_record
    )
