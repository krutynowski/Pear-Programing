from flask_wtf import Form
from wtforms import StringField, PasswordField, FloatField
from  wtforms.validators import DataRequiered, Length 

class UserForm(Form):
  username = StringField('username', validators = [DataRequiered() ])
  password = PasswordField('password', validators = [DataRequiered(), Length(6) ])


class FishForm(Form):
  type = StringField('type', validators = [DataRequiered() ])
  weight = PasswordField('weight', validators = [DataRequiered(), Length(6) ])  