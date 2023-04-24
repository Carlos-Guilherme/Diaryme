from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fgdsfgdjkhjklutiywrfdsv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.app_context().push()

database = SQLAlchemy(app)
#database.create_all()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from diario import routes