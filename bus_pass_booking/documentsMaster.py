from flask import Blueprint, render_template, request
import pymysql

DocumentsMaster = Blueprint("DocumentsMaster", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewDocumentID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(document_id) FROM documentsMaster")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


@DocumentsMaster.route('/documentsMaster', methods=['GET', 'POST'])
def documents_master_index():

    documentlist = []
    applicationlist = []

    document_id = request.args.get('document_id', '')
    application_id = request.args.get('application_id', '')
    uploaded_date = request.args.get('uploaded_date', '')

    is_record = bool(document_id)

    if not is_record:
        document_id = GetNewDocumentID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            document_id = request.form['document_id']
            application_id = request.form['application_id']
            uploaded_date = request.form['uploaded_date']

            if btn == 'Insert':
                cursor.execute(
                    "INSERT INTO documentsMaster VALUES (%s,%s,%s)",
                    (document_id, application_id, uploaded_date)
                )
                conn.commit()

            elif btn == 'Update':
                cursor.execute(
                    "UPDATE documentsMaster SET application_id=%s, uploaded_date=%s WHERE document_id=%s",
                    (application_id, uploaded_date, document_id)
                )
                conn.commit()

            elif btn == 'Delete':
                cursor.execute(
                    "DELETE FROM documentsMaster WHERE document_id=%s",
                    (document_id,)
                )
                conn.commit()

            document_id = GetNewDocumentID()
            application_id = ''
            uploaded_date = ''
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()

    # Dropdown
    cursor.execute("SELECT * FROM applications")
    applicationlist = cursor.fetchall()

    # Table Display (NO JOIN)
    cursor.execute("SELECT * FROM documentsMaster")
    documentlist = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "documentsMaster.html",
        documentlist=documentlist,
        applicationlist=applicationlist,
        document_id=document_id,
        application_id=application_id,
        uploaded_date=uploaded_date,
        is_record=is_record
    )
