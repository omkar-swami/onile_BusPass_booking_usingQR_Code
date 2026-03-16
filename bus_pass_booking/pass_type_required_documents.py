from flask import Blueprint, render_template, request
import pymysql

DocRequired = Blueprint("DocRequired", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewDocReqID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(doc_req_id) FROM pass_type_required_documents")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1

@DocRequired.route('/pass_type_required_documents', methods=['GET', 'POST'])
def doc_required_index():

    docreq_list = []
    pass_typelist = []
    documentlist = []
    usertypelist = []

    doc_req_id = request.args.get('doc_req_id', '')
    pass_type_id = request.args.get('pass_type_id', '')
    document_type_id = request.args.get('document_type_id', '')
    user_type_id = request.args.get('user_type_id', '')

    is_record = bool(doc_req_id)

    if not is_record:
        doc_req_id = GetNewDocReqID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            doc_req_id = request.form['doc_req_id']
            pass_type_id = request.form['pass_type_id']
            document_type_id = request.form['document_type_id']
            user_type_id = request.form['user_type_id']

            if btn == 'Insert':
                cursor.execute(
                    "INSERT INTO pass_type_required_documents VALUES (%s,%s,%s,%s)",
                    (doc_req_id, pass_type_id, document_type_id, user_type_id)
                )
                conn.commit()

            elif btn == 'Update':
                cursor.execute(
                    """UPDATE pass_type_required_documents 
                       SET pass_type_id=%s,
                           document_type_id=%s,
                           user_type_id=%s
                       WHERE doc_req_id=%s""",
                    (pass_type_id, document_type_id, user_type_id, doc_req_id)
                )
                conn.commit()

            elif btn == 'Delete':
                cursor.execute(
                    "DELETE FROM pass_type_required_documents WHERE doc_req_id=%s",
                    (doc_req_id,)
                )
                conn.commit()

            doc_req_id = GetNewDocReqID()
            pass_type_id = ''
            document_type_id = ''
            user_type_id = ''
            is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pass_type")
    pass_typelist = cursor.fetchall()

    cursor.execute("SELECT * FROM document_types")
    documentlist = cursor.fetchall()

    cursor.execute("SELECT * FROM user_type")
    usertypelist = cursor.fetchall()

    cursor.execute("SELECT * FROM pass_type_required_documents")
    docreq_list = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "pass_type_required_documentsListReport.html",
        docreq_list=docreq_list,
        pass_typelist=pass_typelist,
        documentlist=documentlist,
        usertypelist=usertypelist,
        doc_req_id=doc_req_id,
        pass_type_id=pass_type_id,
        document_type_id=document_type_id,
        user_type_id=user_type_id,
        is_record=is_record
    )
