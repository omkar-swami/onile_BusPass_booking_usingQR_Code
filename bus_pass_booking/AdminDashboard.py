from flask import Blueprint, render_template, request, session
import pymysql

AdminDashboard= Blueprint("AdminDashboard", __name__)
@AdminDashboard.route('/AdminDashboard', methods=['GET', 'POST'])
def AdminDashboard_index():
    return  render_template("AdminDashboard.html")