from _ast import Pass

from flask import Flask,render_template,session

from datetime import timedelta
from UserType import UserType
from  Users import Users
from routes import Routes
from pass_type import PassType
from pass_discounts import PassDiscounts
from applications import Applications
from document_types import DocumentTypes
from pass_type_required_documents import DocRequired
from documentsMaster import DocumentsMaster
from documentDetails import DocumentDetails
from payments import Payments
from bus_pass import BusPass


from ListReports import ListReports
from DynamicReports import DynamicReports
from DateWiseReports import DateWiseReports

from UserLogIn import UserLogIn
from userRegistration import userRegistration
from AdminLogIn import AdminLogIn
from UserDashbaord import UserDashbaord
from AdminDashboard import AdminDashboard

from SearchAllRoutes import  SearchAllRoutes
from SearchDetails import SearchDetails
from buspassApplication import buspassApplication
from Invoice import Invoice

from UsersPassApplications import UsersPassApplications
from QRcodeGenrator import QRcodeGenrator
from ApplicationRequest import ApplicationRequest
from ViewDocuments import ViewDocuments
from ScanQRCode import ScanQRCode
from Logout import Logout
app = Flask(__name__)
app.secret_key="SoftTech#2011"
app.permanent_session_lifetime = timedelta(hours=12)

app.register_blueprint(UserType)
app.register_blueprint(Users)
app.register_blueprint(Routes)
app.register_blueprint(PassType)
app.register_blueprint(PassDiscounts)
app.register_blueprint(Applications)
app.register_blueprint(DocumentTypes)
app.register_blueprint(DocRequired)
app.register_blueprint(DocumentsMaster)
app.register_blueprint(DocumentDetails)
app.register_blueprint(Payments)
app.register_blueprint(BusPass)


app.register_blueprint(ListReports)
app.register_blueprint(DynamicReports)
app.register_blueprint(DateWiseReports)

app.register_blueprint(UserLogIn)
app.register_blueprint(AdminLogIn)
app.register_blueprint(UserDashbaord)

app.register_blueprint(userRegistration)
app.register_blueprint(AdminDashboard)


app.register_blueprint(SearchAllRoutes)
app.register_blueprint(SearchDetails)
app.register_blueprint(buspassApplication)
app.register_blueprint(Invoice)
app.register_blueprint(UsersPassApplications)
app.register_blueprint(QRcodeGenrator)
app.register_blueprint(Logout)
app.register_blueprint(ApplicationRequest)
app.register_blueprint(ViewDocuments)
app.register_blueprint(ScanQRCode)
@app.route("/")
def index():
     return render_template('Home.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5008)