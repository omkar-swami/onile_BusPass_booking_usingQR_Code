from flask import Blueprint, render_template, request
import pymysql

DynamicReports = Blueprint("DynamicReports", __name__)
def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )
conn = connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM user_type")
usertypelist = cursor.fetchall()

cursor.execute("SELECT * FROM pass_type")
passtypelist = cursor.fetchall()
cursor.execute("SELECT * FROM applications")
applicationlist = cursor.fetchall()
cursor.execute("SELECT * FROM document_types")
document_typeslist = cursor.fetchall()
cursor.execute("SELECT * FROM documentsMaster")
documentsMasterlist = cursor.fetchall()

@DynamicReports.route('/UserDynamicReport', methods=['GET', 'POST'])
def UserDynamicReport():
    userlist=[]
    if request.method == 'POST':
        user_type_id = request.form.get('user_type_id')
        cursor.execute("select user_id,full_name,email,mobile,password,address,user_type.type_name,created_at from users,user_type where users.user_type_id=user_type.user_type_id and users.user_type_id=%s",(user_type_id))
        userlist = cursor.fetchall()

    return  render_template("DynamicReports/UserDynamicReport.html",usertypelist=usertypelist,userlist=userlist)



@DynamicReports.route('/Bus_PassDynamicReport', methods=['GET', 'POST'])
def Bus_PassDynamicReport():
    buspasslist=[]
    if request.method == 'POST':
        pass_type_id = request.form.get('pass_type_id')
        application_id=request.form.get('application_id')
        if application_id!="0" and pass_type_id!="0":
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
                    AND bus_pass.pass_type_id=%s
                      AND bus_pass.application_id=%s;
                    
                         """, (pass_type_id,application_id))
        elif application_id!="0":
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
                                    AND bus_pass.application_id=%s;
                                         """, (application_id,))
        elif pass_type_id!="0":
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
                                    AND bus_pass.pass_type_id=%s
                                    ;
                                         """, (pass_type_id,))



        buspasslist = cursor.fetchall()


    return  render_template("DynamicReports/Bus_PassDynamicReport.html",passtypelist=passtypelist,applicationlist=applicationlist,buspasslist=buspasslist)

@DynamicReports.route('/documents_MasterDynamicReport', methods=['GET', 'POST'])
def documentsMasterDynamicReport():
    documentlist=[]
    if request.method == 'POST':
        application_id = request.form.get('application_id')
        cursor.execute("select * from documentsMaster where application_id=%s",(application_id,))
        documentlist = cursor.fetchall()

    return  render_template("DynamicReports/documents_MasterDynamicReport.html",applicationlist=applicationlist,documentlist=documentlist)


@DynamicReports.route('/documentDetailsDynamicReport', methods=['GET', 'POST'])
def documentDetailsDynamicReport():
    documentDetailslist = []
    if request.method == 'POST':
        document_id  = request.form.get('document_id')
        document_type_id  = request.form.get('document_type_id')
        if document_id != "0" and document_type_id != "0":
            cursor.execute(""" select documentDet_id,document_id,document_name,photo 
                        from documentDetails,document_types 
                        where  documentDetails.document_type_id = document_types.document_type_id
                        and documentDetails.document_id =%s
                        and documentDetails.document_type_id =%s;
                         """, (document_id, document_type_id))
        elif document_id != "0":
            cursor.execute("""select documentDet_id,document_id,document_name,photo 
                        from documentDetails,document_types 
                        where  documentDetails.document_type_id = document_types.document_type_id
                        and documentDetails.document_id =%s
                                         """, (document_id,))
        elif document_type_id != "0":
            cursor.execute("""
            select documentDet_id,document_id,document_name,photo 
                        from documentDetails,document_types 
                        where  documentDetails.document_type_id = document_types.document_type_id
                        and documentDetails.document_type_id =%s
            """, (document_type_id,))

        documentDetailslist = cursor.fetchall()

    return render_template("DynamicReports/documentDetailsDynamicReport.html", document_typeslist=document_typeslist,
                           documentsMasterlist=documentsMasterlist, documentDetailslist=documentDetailslist)
@DynamicReports.route('/PaymentsDynamicReport', methods=['GET', 'POST'])
def Payments_DynamicReportDynamicReport():
    paymentlist=[]
    if request.method == 'POST':
        application_id = request.form.get('application_id')
        cursor.execute("select * from payments where application_id=%s",(application_id,))
        paymentlist = cursor.fetchall()

    return  render_template("DynamicReports/PaymentsDynamicReport.html",applicationlist=applicationlist,paymentlist=paymentlist)
