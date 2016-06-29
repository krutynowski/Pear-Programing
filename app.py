from flask import Flask, redirect, url_for, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from forms import UserForm
from flask_wtf import CsrfProtect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
bcrypt = Bcrypt

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_fishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.Text(), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    fishes = db.relationship('Fish', backref='user', lazy='dynamic')

def __init__(self, username, password):
    self.username = username
    self.password = bcrypt.generate_password_hash(password).decode('utf-8')



class Fish(db.Model):

    __tablename__ = 'fishes'

    id = db.Column(db.Integer, primary_key= True)
    type = db.Column(db.Text(), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, type, weight, user_id):
      self.type = type
      self.weight = weight
      self.user_id = user_id

#Routes to get to users/new, get/login, post/users, post/loin, get/users 
@app.route('/')
def root():
   return redirect(url_for('login')) 


@app.route('/login', methods= ['GET', 'POST'])
def login():
  error = None 
  form = LoginForm()

@app.route('/users/new')
def signup():
  return render_template('/users/new.html')



@app.route('/users', methods =['GET'])
def index():
  return render_template('index.html', users = Users.query.all())

@app.route('/users', methods =['POST'])

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)



