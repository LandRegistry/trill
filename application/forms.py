from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField, SelectField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email
    
class SigninForm(Form):
    username = TextField('Username', validators=[Required(),validators.Length(max=100, message=(u'Username'))])
    password = PasswordField('Password', validators=[Required(),validators.Length(max=100, message=(u'Password'))])
    #remember_me = BooleanField('Remember me', default = False)
