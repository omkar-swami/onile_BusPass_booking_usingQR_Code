from flask import Blueprint, render_template, request, session,redirect,url_for
import pymysql
import  os
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
def GetNewApplicationID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(application_id) FROM applications")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1

def GetNewPaymentID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(payment_id) FROM payments")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1

def GetNewPassID():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(pass_id) FROM bus_pass")
    rs = cursor.fetchone()
    maxid = rs[0]

    if maxid is None:
        maxid = 0

    cursor.close()
    conn.close()
    return int(maxid) + 1

buspassApplication = Blueprint("buspassApplication", __name__)
@buspassApplication.route('/buspassApplication', methods=['GET', 'POST'])
def buspassApplication_index():
    conn = connection()
    cursor = conn.cursor()
    reqdocuments=[]
    userData=[]
    routeData=[]
    passinfo=[]
    route_id=0
    user_type_id=0
    pass_type_id=0
    dis_per=0
    discount_amount=0
    original_price=0
    final_amount=0
    application_id=0
    if request.method == 'GET':
        user_id=0
        application_id=GetNewApplicationID()
        route_id = request.args.get('route_id')
        user_type_id = request.args.get('user_type_id')
        pass_type_id = request.args.get('pass_type_id')
        original_price=request.args.get('original_price')
        dis_per=request.args.get('dis_per')
        discount_amount=request.args.get('discount_amount')
        final_amount=request.args.get('final_amount')
        if 'user_id' in session:
            user_id=session['user_id']
        else:
            return redirect(url_for("UserLogIn.UserLogIn_index"))
        cursor.execute("select user_id,full_name,email,mobile,password,address,user_type.type_name,created_at from users,user_type where users.user_type_id=user_type.user_type_id and users.user_id=%s ",(user_id,))
        userData=cursor.fetchall()

        cursor.execute("select * from routes where route_id=%s", (route_id,))
        routeData=cursor.fetchall()

        cursor.execute("""
               SELECT 
            doc_req_id,
            pass_type_required_documents.document_type_id,
            document_name,
            pass_type_required_documents.pass_type_id,
            pass_type_required_documents.user_type_id,
            user_type.type_name,
            pass_type.pass_name
        FROM 
            pass_type_required_documents,
            document_types,
            user_type,
            pass_type
        WHERE 
            pass_type_required_documents.document_type_id = document_types.document_type_id
        AND pass_type_required_documents.user_type_id = user_type.user_type_id
        AND pass_type_required_documents.pass_type_id = pass_type.pass_type_id
        and pass_type_required_documents.pass_type_id=%s 
        and pass_type_required_documents.user_type_id=%s ;
        """,(pass_type_id,user_type_id,))
        reqdocuments = cursor.fetchall()
        cursor.execute("select * from pass_type where pass_type_id =%s", (pass_type_id ,))
        passinfo=cursor.fetchall()

    if request.method == 'POST':
        conn = connection()
        cursor = conn.cursor()
        user_id = session['user_id']
        route_id = request.form.get("route_id")
        pass_type_id = request.form.get("pass_type_id")
        final_amount = request.form.get("final_amount")
        application_id = GetNewApplicationID()

        cursor.execute("""
                    INSERT INTO applications
                    (application_id, user_id, pass_type_id, route_id,
                      status, applied_date)
                    VALUES (%s,%s,%s,%s,'Pending',NOW())
                """, (application_id, user_id, pass_type_id,
                      route_id))
        conn.commit()
        document_id = GetNewDocumentID()

        cursor.execute("""
                    INSERT INTO documentsMaster
                    VALUES (%s,%s,NOW())
                """, (document_id, application_id))
        doc_type_ids = request.form.getlist("doc_type_id[]")
        files = request.files.getlist("documents[]")

        UPLOAD_FOLDER = "static/Uploads"
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        for i in range(len(files)):

            file = files[i]
            doc_type_id = doc_type_ids[i]

            if file and file.filename != "":
                documentDet_id = GetNewDocumentDetID()
                document_type_name=[]
                cursor.execute("select * from document_types where document_type_id =%s", (doc_type_id,))
                document_type_name=cursor.fetchall()
                ext = file.filename.split('.')[-1]
                new_filename = f"A{application_id}_U{user_id}_{document_type_name[0][1]}.{ext}"

                filepath = os.path.join(UPLOAD_FOLDER, new_filename)
                file.save(filepath)
                cursor.execute("""
                                                   INSERT INTO documentDetails
                                                   VALUES (%s,%s,%s,%s)
                                               """, (documentDet_id, document_id,
                                                     doc_type_id, new_filename))
                conn.commit()
        payment_id = GetNewPaymentID()
        cursor.execute(
            "INSERT INTO payments VALUES (%s,%s,%s,NOW())",
            (payment_id, application_id, final_amount)
        )
        conn.commit()
        pass_id = GetNewPassID()
        base_amount = request.form.get("original_amount")
        discount_amount = request.form.get("discount_amount")
        expiry_date = request.form.get("expiryDate")
        cursor.execute(
            "INSERT INTO bus_pass VALUES (%s,%s,%s,%s,%s,%s,NOW(),%s,%s)",
            (pass_id, pass_type_id, application_id,
             base_amount, discount_amount,
             final_amount, expiry_date,'Pending')
        )
        conn.commit()
        session["pass_id"]=pass_id
        return  redirect(url_for("Invoice.Invoice_index",
                                 pass_id=pass_id,
                                 ))



    return render_template("Search/buspassApplication.html",
                           reqdocuments=reqdocuments,
                           userData=userData,
                           routeData=routeData,
                           passinfo=passinfo,
                           original_price=original_price,
                           dis_per=dis_per,
                           discount_amount=discount_amount,
                           final_amount=final_amount, application_id=application_id)
