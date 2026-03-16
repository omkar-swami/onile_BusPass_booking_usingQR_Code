from flask import Blueprint, render_template, request
import pymysql

DateWiseReports = Blueprint("DateWiseReports", __name__)
def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        database='bus_pass_booking',
        port=3308
    )

@DateWiseReports.route("/usersDateWiseReports", methods=['GET', 'POST'])
def usersDateWiseReports():
    userlist=[]
    if request.method == 'POST':
        FDate=request.form['FDate']
        TDate=request.form['TDate']
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(
            """select user_id,full_name,email,
            mobile,password,address,user_type.type_name,created_at 
            from users,user_type 
            where users.user_type_id=user_type.user_type_id
            and created_at >=%s and created_at <=%s """,(FDate,TDate,))
        userlist = cursor.fetchall()
    return  render_template("DateWiseReports/usersDateWiseReports.html",userlist=userlist)

@DateWiseReports.route("/documentsMasterDateWiseReports", methods=['GET', 'POST'])
def documentsMasterDateWiseReports():
    documentlist=[]
    if request.method == 'POST':
        FDate=request.form['FDate']
        TDate=request.form['TDate']
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(
            """select document_id,full_name,uploaded_date 
            from documentsmaster,applications,users 
            where documentsmaster.application_id=applications.application_id 
            and applications.user_id=users.user_id
            and uploaded_date >=%s and uploaded_date <=%s """,(FDate,TDate,))
        documentlist = cursor.fetchall()
    return  render_template("DateWiseReports/documentsMasterDateWiseReports.html",documentlist=documentlist)

@DateWiseReports.route("/paymentsDateWisereports", methods=['GET', 'POST'])
def paymentsDateWisereports():
    paymentlist=[]
    if request.method == 'POST':
        FDate=request.form['FDate']
        TDate=request.form['TDate']
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(
            """select payment_id,full_name,amount,payment_date 
            from payments,applications,users 
            where payments.application_id=applications.application_id 
            and applications.user_id=users.user_id
            and payment_date  >=%s and payment_date  <=%s """,(FDate,TDate,))
        paymentlist = cursor.fetchall()
    return  render_template("DateWiseReports/paymentsDateWisereports.html",paymentlist=paymentlist)



@DateWiseReports.route("/BusPassDateWisereports", methods=['GET', 'POST'])
def BusPassDateWisereports():
    buspasslist=[]
    if request.method == 'POST':
        btn=request.form['btn']
        FDate=request.form['FDate']
        TDate=request.form['TDate']
        conn = connection()
        cursor = conn.cursor()
        if btn=="issue":
            cursor.execute(
                """SELECT 
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
                and issue_date  >=%s and issue_date  <=%s """, (FDate, TDate,))
        else:
            cursor.execute(
                """ SELECT 
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
                and expiry_date  >=%s and expiry_date  <=%s """, (FDate, TDate,))

        buspasslist = cursor.fetchall()
    return  render_template("DateWiseReports/BusPassDateWisereports.html",buspasslist=buspasslist)
