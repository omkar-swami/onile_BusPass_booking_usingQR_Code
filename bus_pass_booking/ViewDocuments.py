from flask import Blueprint, render_template, request
import pymysql

ViewDocuments = Blueprint("ViewDocuments", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

@ViewDocuments.route('/ViewDocuments', methods=['GET', 'POST'])
def ViewDocuments_index():

    application_id = request.args.get('application_id')

    documentMaster = []
    doumentDetail = []

    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM documentsMaster WHERE application_id=%s", (application_id,))
    documentMaster = cursor.fetchall()

    if len(documentMaster) > 0:

        document_id = documentMaster[0][0]

        cursor.execute("""
        SELECT documentDet_id, document_id, documentdetails.document_type_id, document_name, photo
        FROM documentdetails, document_types
        WHERE documentdetails.document_type_id = document_types.document_type_id
        AND documentdetails.document_id = %s
        """, (document_id,))

        doumentDetail = cursor.fetchall()

    return render_template(
        "Search/ViewDocuments.html",
        documentMaster=documentMaster,
        doumentDetail=doumentDetail
    )