from flask_wtf import Form
from wtforms import StringField, PasswordField, FloatField
from  wtforms.validators import DataRequired, Length 

class UserForm(Form):
  username = StringField('username', validators = [DataRequired() ])
  password = PasswordField('password', validators = [DataRequired(), Length(6) ])


class FishForm(Form):
  type = StringField('type', validators = [DataRequired() ])
  weight = PasswordField('weight', validators = [DataRequired(), Length(6) ])  