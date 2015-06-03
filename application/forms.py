from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField, SelectField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email

class SigninForm(Form):
    username = TextField('Username', validators=[Required(),validators.Length(max=50, message=(u'Username too long'))])
    password = PasswordField('Password', validators=[Required(),validators.Length(max=20, message=(u'Password too long'))])
    remember_me = BooleanField('Remember me', default = False)
    
class EmailForm(Form):
    email = TextField('Username', validators=[Required(), Email()])

class PasswordForm(Form):
    password = PasswordField('Password', validators=[Required(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm', validators=[Required()])

