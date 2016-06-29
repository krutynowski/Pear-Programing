from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm

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

@app.route('/users', method =['POST'])

@app.route('/logout')


def create_users():
  form = UserForm() 
  new_user = User(form.username.data, form.password.data)
  db.session.add(new_user)
  db.session.commit()
  return redirect(url_for('index')








if __name__ == '__main__':
    app.run(debug=True, port=3000)