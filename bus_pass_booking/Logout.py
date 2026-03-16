from flask import Blueprint, render_template, request,session,redirect,url_for
import pymysql

Logout = Blueprint("Logout", __name__)
@Logout.route('/Logout', methods=['GET', 'POST'])
def Logout_index():
    session.clear()
    return redirect(url_for('index'))
