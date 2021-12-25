from Expresso import db, login_manager
from Expresso import bcrypt
from flask_login import UserMixin 


@login_manager.user_loader
def load_user(employee_id):
    return Employee.query.get(str(employee_id))

class Employee(db.Model, UserMixin):
    __tablename__="employee"
    id = db.Column(db.String(length=30), nullable=False, unique=True, primary_key=True)
    email_address = db.Column(db.String(length=30), nullable =False, unique=True)
    surname = db.Column(db.String(length=30), nullable =False, unique=True)
    firstname = db.Column(db.String(length=30), nullable =False, unique=True)
    middlename = db.Column(db.String(length=30), nullable =False, unique=True)
    employee_password = db.Column(db.String(length=650), nullable =False)

    @property
    def password(self):
        return self.employee_password

    #@password.setter
    #def password(self, plain_text_password):
     #   self.employee_password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_match(self, attempted_password):
        return bcrypt.check_password_hash(self.employee_password , attempted_password)


class ExpressoUser(db.Model, UserMixin):
    __tablename__="expresso_user"
    userid = db.Column(db.String(length=30), primary_key=True)
    region = db.Column(db.String(length=30))
    tenure = db.Column(db.String(length=30))	
    montant = db.Column(db.Float())
    frequence_rech = db.Column(db.Integer())
    revenue = db.Column(db.Float())
    arpu_segment = db.Column(db.Float())
    frequence = db.Column(db.Integer())
    data_volume = db.Column(db.Integer())	
    on_net = db.Column(db.Integer())
    orange	= db.Column(db.Integer())
    tigo = db.Column(db.Integer())
    zone1 = db.Column(db.Integer())
    zone2 = db.Column(db.Integer())
    mrg	= db.Column(db.String(length=30))
    regularity	= db.Column(db.Integer())
    top_pack = db.Column(db.String(length=30))
    freq_top_pack = db.Column(db.Integer())


