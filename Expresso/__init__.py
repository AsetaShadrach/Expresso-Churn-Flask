from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a57c3b7d5cd1f328c883821a88'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:password@localhost/expresso_churn'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'


from Expresso import routes