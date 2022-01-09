from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField,SelectField
from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from Expresso.models import Employee

class UserDataForm(FlaskForm):
    user_id = StringField(label="ID", validators=[DataRequired()])
    REGIONS = [ (""),("DAKAR"),("DIOURBEL"),("FATICK"),("KAFFRINE"),
                ("KAOLACK"),("KEDOUGOU"),("KOLDA"),("LOUGA"),("MATAM"),
                ("SAINT-LOUIS"),("SEDHIOU"),("TAMBACOUNDA"),("THIES"),("ZIGUINCHOR")]

    region = SelectField(choices=REGIONS)

    TENURES = [ (""),("D 3-6 month"),("E 6-9 month"),("F 9-12 month"),
                ("G 12-15 month"),("H 15-18 month"),("I 18-21 month"),
                ("J 21-24 month	"),("K > 24 month")]
    tenure = SelectField(choices=TENURES)	
    montant = FloatField(label="Montant")
    frequence_rech = IntegerField(label="Freq Rech")
    revenue = FloatField(label="Revenue")
    arpu_segment = FloatField(label="ARPU-Segment")
    frequence = IntegerField(label="Frequence")
    data_volume = IntegerField(label=" Data Volume")	
    on_net = IntegerField(label="No. On-Net calls")
    orange	= IntegerField(label="No of calls to Orange")
    tigo = IntegerField(label="No. of calls to Tigo")
    zone1 = IntegerField(label="No. of calls to Zone1")
    zone2 = IntegerField(label="No. of calls to Zone2")
    
    MIGRATED=[("NO"),("YES")]
    mrg	= SelectField(choices=MIGRATED)
    
    regularity	= IntegerField(label="Regularity")
    top_pack = StringField(label="Top Pack")
    freq_top_pack = IntegerField(label="Frequency of top pack")
    user_add = SubmitField(label="Add User to Record")
    user_predict = SubmitField(label="Predict Probability of User Churn")
    add_prediction = SubmitField(label="Add prediction to Database")

class LoginForm(FlaskForm):
    employee_id = StringField( label="Employee ID",  validators = [DataRequired()])
    employee_password = PasswordField(label="Password",  validators = [DataRequired()])
    employee_login = SubmitField(label="Login")


class ModalAccessGrant(FlaskForm):
    employee_id = StringField( label="Employee ID",  validators = [DataRequired()])
    employee_email = StringField(   label="Employee Email", 
                                    validators = [Email(),
                                    DataRequired()])
    access_confirm = SubmitField(label="Go to Registration")



class RegistrationForm(FlaskForm):
    employee_id = StringField( label="Employee ID",  validators = [DataRequired()])
    employee_email = StringField(   label="Employee Email", 
                                    validators = [Length(min=8), 
                                    Email(),
                                    DataRequired()])
    employee_sname = StringField(label="Surname" , validators=[DataRequired()])
    employee_fname = StringField(label="First Name" , validators=[DataRequired()])
    employee_mname = StringField(label="Middle Name" , validators=[DataRequired()])
    employee_password = PasswordField(  label="Password",  
                                        validators = [DataRequired()])
    employee_password_confirm = PasswordField(label="Confirm Password"  ,
                                                validators = [EqualTo('employee_password'),
                                                                DataRequired()])
    employee_create = SubmitField(label="Create Account")

class AddUserRecord(FlaskForm):
    submit = SubmitField(label="Add User Record")

class AddPredictionRecord(FlaskForm):
    submit = SubmitField(label="Add Prediction")




