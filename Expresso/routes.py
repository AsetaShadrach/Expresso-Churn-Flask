import json
import requests 
from Expresso import app, bcrypt
from flask import render_template, url_for, flash, redirect, request
from Expresso.forms import UserDataForm, LoginForm, ModalAccessGrant, RegistrationForm
import os
from flask_login import login_user, logout_user, login_required, current_user
from Expresso import db
from Expresso.models import Employee, ExpressoUser
from Expresso.helpers.prediction_helper import get_prediction

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/userinfo', methods =['GET','POST'])
@login_required
def userinfo_page():
    form = UserDataForm()
    return render_template('UserInfo.html', form = form)


@app.route('/login', methods =['GET','POST'])
def login_page():
    empl_login_form = LoginForm()
    
    if empl_login_form.validate_on_submit():
        empl_id = request.form.get('employee_id')
        empl_password = request.form.get('employee_password')
        attempted_employee = Employee.query.filter_by(id=empl_id).first()

        if attempted_employee and attempted_employee.check_password_match(empl_password):
            login_user(attempted_employee)
            flash(f"Logged in as {attempted_employee.firstname}", category='success')
            return redirect(url_for('datainsights_page'))
        else:
            flash("Incorrect Username or Password !", category='danger')
            

    return render_template('login.html', form = empl_login_form)



@app.route('/register-access', methods=['GET','POST'])
def reg_access_page():
    registration_access = ModalAccessGrant()  
    if registration_access.validate_on_submit():
        attempted_empl = Employee.query.filter_by(id=registration_access.employee_id.data ,
                                    email_address=registration_access.employee_email.data).first()
        if attempted_empl :
            return redirect(url_for('accountsetup_page'))
        else:
            flash("Invalid Username or Email !", category='danger')
        
    return render_template('reg_access.html',registration_access=registration_access)


@app.route('/account-creation', methods =['GET','POST'])
def accountsetup_page():

    form = RegistrationForm()
    if form.validate_on_submit():
        employee_details = Employee.query.filter(Employee.id == form.employee_id.data , 
                                                Employee.email_address == form.employee_email.data).first()
        
        if employee_details:
            employee_details.surname = form.employee_sname.data
            employee_details.firstname = form.employee_fname.data
            employee_details.middlename = form.employee_mname.data
            employee_details.employee_password = bcrypt.generate_password_hash(form.employee_password.data).decode('utf-8')
                                  
            db.session.commit()
            login_user(employee_details)
            flash ("Account Successfully Created", category='success')
            return redirect(url_for('datainsights_page'))
        else:
            flash(f"Wrong Employee ID or Email" , category='danger')

    if form.errors !={}:
        for error_msg in form.errors.values():
            flash(f"Error : {error_msg}", category='danger')

    return render_template('AccountSetup.html', form = form)


@app.route('/datainsights')
@login_required
def datainsights_page():
    image_names = os.listdir(os.path.join('Expresso','static','images','charts'))
    return render_template('DataInsights.html' , image_names=image_names)
    

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have logged out !", category='info')
    return redirect(url_for('login_page'))

@app.route('/trial-prediction', methods=['GET','POST'])
def trial_prediction_page():
    form = UserDataForm()
    prediction = ""
    if request.method=="POST":
        prediction = get_prediction(request)
        return render_template("trial_prediction.html", form = form, prediction=prediction)
    return render_template("trial_prediction.html", form = form , prediction=prediction )


if __name__ == '__main__':
    app.run()