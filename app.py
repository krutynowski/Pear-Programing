from flask import Flask, redirect, url_for, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from forms import UserForm
from flask_wtf import CsrfProtect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)


# configuring our managers
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'login'
CsrfProtect(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'shhhh'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_fishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model, UserMixin):

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


# User Helper
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

#Routes to get to users/new, get/login, post/users, post/loin, get/users 
@app.route('/')
def root():
   return redirect(url_for('login')) 

@app.route('/users', methods =['GET'])
@login_required
def index():
  return render_template('users/index.html', users = User.query.all())

@app.route('/users/new')
def new():
  form = UserForm()
  return render_template('users/new.html', form = form)

@app.route('/users', methods =['POST'])
def create():
  form = UserForm()
  if form.validate_on_submit():
    new_user = User(form.username.data, form.password.data)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    flash('User Createddd')
    return redirect(url_for('index'))

  return render_template('users/new.html', form=form)

@app.route('/login', methods= ['GET', 'POST'])
def login():
  error = None 
  form = UserForm()
  if form.validate_on_submit():
    found_user = User.query.filter_by(username=form.username.data).first()
    if found_user:
      is_authenticated = bcrypt.check_password_hash(found_user.password, form.password.data)
      if is_authenticated:
        flash('User Logged in!')
        login_user(found_user)
        return redirect(url_for('index'))
      else:
        error = "Invalid Username or Password"  
  return render_template('users/login.html', form=form, error=error)


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)



