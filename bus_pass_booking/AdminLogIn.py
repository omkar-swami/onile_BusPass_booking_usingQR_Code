from flask import Blueprint, render_template, request, session, redirect, url_for
import pymysql

AdminLogIn = Blueprint("AdminLogIn", __name__)

@AdminLogIn.route('/AdminLogIn', methods=['GET', 'POST'])
def AdminLogIn_index():
    error = ""

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin" and password == "123":
            session["role"] = "Admin"
            session["islogin"] = True

            return redirect(url_for("AdminLogIn.AdminDashboard"))  # Redirect instead of render
        else:
            error = "Invalid email or password"

    return render_template("AdminLogIn.html", error=error)

@AdminLogIn.route('/AdminDashboard')
def AdminDashboard():
    if session.get("islogin"):
        return render_template("AdminDashboard.html")
    else:
        return redirect(url_for("AdminLogIn.AdminLogIn_index"))