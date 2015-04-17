from application import app
from flask import render_template
#, flash, redirect, request, session, make_response

'''@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/view')
def view_skills():
    return render_template('view_skills.html')

@app.route('/edit')
def edit_skills():
    return render_template('edit_skills.html')

@app.route('/admin')
def admin_func():
    return render_template('admin_func.html')'''

@app.route('/')
def view_skills():
    return render_template('test.html')
