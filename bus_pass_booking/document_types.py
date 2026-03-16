from flask import Blueprint, render_template, request
import pymysql

DocumentTypes = Blueprint("DocumentTypes", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

def GetNewDocumentTypeID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(document_type_id) FROM document_types")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1


def clear_textbox():
    return '', ''


@DocumentTypes.route('/document_types', methods=['GET', 'POST'])
def document_types_index():

    documentlist = []
    document_type_id = request.args.get('document_type_id', '')
    document_name = request.args.get('document_name', '')
    is_record = bool(document_type_id)

    if not is_record:
        document_type_id = GetNewDocumentTypeID()

    if request.method == 'POST':
        btn = request.form['btn']
        conn = connection()
        cursor = conn.cursor()

        try:
            document_type_id = request.form['document_type_id']
            document_name = request.form['document_name']

            if btn == 'Insert':
                cursor.execute(
                    "INSERT INTO document_types VALUES (%s,%s)",
                    (document_type_id, document_name)
                )
                conn.commit()
                document_type_id, document_name = clear_textbox()
                document_type_id = GetNewDocumentTypeID()
                is_record = False

            elif btn == 'Update':
                cursor.execute(
                    "UPDATE document_types SET document_name=%s WHERE document_type_id=%s",
                    (document_name, document_type_id)
                )
                conn.commit()
                document_type_id, document_name = clear_textbox()
                document_type_id = GetNewDocumentTypeID()
                is_record = False

            elif btn == 'Delete':
                cursor.execute(
                    "DELETE FROM document_types WHERE document_type_id=%s",
                    (document_type_id,)
                )
                conn.commit()
                document_type_id, document_name = clear_textbox()
                document_type_id = GetNewDocumentTypeID()
                is_record = False

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM document_types")
    documentlist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "document_types.html",
        documentlist=documentlist,
        document_type_id=document_type_id,
        document_name=document_name,
        is_record=is_record
    )
