from flask import Blueprint, render_template, request
import pymysql

ListReports = Blueprint("ListReports", __name__)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

@ListReports.route('/UserType_ListReports', methods=['GET'])
def user_type_ListReports():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_type")
    usertypelist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/UserTypeListReport.html",
        usertypelist=usertypelist
    )
@ListReports.route('/Users_ListReport', methods=['GET'])
def userS_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select user_id,full_name,email,mobile,password,address,user_type.type_name,created_at from users,user_type where users.user_type_id=user_type.user_type_id")
    userlist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/Users_ListReport.html",
        userlist=userlist
    )
@ListReports.route('/RoutesListReport', methods=['GET'])
def Routes_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * from routes")
    routelist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/RoutesListReport.html",
        routelist=routelist
    )
@ListReports.route('/Pass_typeListReport', methods=['GET'])
def PassType_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * from pass_type")
    passtypelist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/Pass_typeListReport.html",
        passtypelist=passtypelist
    )
@ListReports.route('/pass_discountsListReport', methods=['GET'])
def pass_discounts_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select discount_id,type_name,pass_name , discount_percentage from pass_discounts,pass_type,user_type where pass_discounts.user_type_id=user_type.user_type_id and pass_discounts.pass_type_id=pass_type.pass_type_id order by discount_id;")
    discountlist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/pass_discountsListReport.html",
        discountlist=discountlist
    )
@ListReports.route('/applicationListReport', methods=['GET'])
def application_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select application_id,full_name,pass_name,route_source,route_destination,status,applied_date from applications,routes,users,pass_type where applications.pass_type_id=pass_type.pass_type_id and applications.route_id=routes.route_id and applications.user_id=users.user_id;")
    applicationlist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/applicationListReport.html",
        applicationlist=applicationlist
    )

@ListReports.route('/document_typeListReport', methods=['GET'])
def document_type_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * from document_types")
    documentlist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/document_typeListReport.html",
        documentlist=documentlist
    )
@ListReports.route('/pass_type_required_documentsListReport', methods=['GET'])
def pass_type_required_documents_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
    doc_req_id,
    pass_name,
    document_name,
    type_name
FROM pass_type_required_documents,
     user_type,
     pass_type,
     document_types
WHERE pass_type_required_documents.pass_type_id = pass_type.pass_type_id
AND pass_type_required_documents.user_type_id = user_type.user_type_id
AND pass_type_required_documents.document_type_id = document_types.document_type_id;
    """)
    docreq_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/pass_type_required_documentsListReport.html",
        docreq_list=docreq_list
    )

@ListReports.route('/documentMasterListReport', methods=['GET'])
def documentMaster_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select document_id,full_name,uploaded_date from documentsmaster,applications,users where documentsmaster.application_id=applications.application_id and applications.user_id=users.user_id;")
    documentlist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/documentMasterListReport.html",
        documentlist=documentlist
    )

@ListReports.route('/documentDetailsListReport', methods=['GET'])
def documentDetails_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select documentDet_id,document_id,document_name,photo from documentdetails,document_types where documentdetails.document_type_id=document_types.document_type_id;")
    documentdetailslist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/documentDetailsListReport.html",
        documentdetailslist=documentdetailslist
    )

@ListReports.route('/paymentsListReport', methods=['GET'])
def payments_ListReport():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select payment_id,full_name,amount,payment_date from payments,applications,users where payments.application_id=applications.application_id and applications.user_id=users.user_id;")
    paymentlist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/paymentsListReport.html",
        paymentlist=paymentlist
    )
@ListReports.route('/bus_passListReport', methods=['GET'])
def bus_pass_ListReport():
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
AND bus_pass.pass_type_id = pass_type.pass_type_id;

     """)
    buspasslist = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "ListReports/bus_passListReport.html",
        buspasslist=buspasslist
    )