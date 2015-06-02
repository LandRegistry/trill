from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField, SelectField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email

'''class LoginForm(Form):
    user_name = StringField('user_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)'''
    
    
class SigninForm(Form):
    username = TextField('Username', validators=[Required(),validators.Length(max=100, message=(u'Username'))])
    password = PasswordField('Password', validators=[Required(),validators.Length(max=100, message=(u'Password'))])
    #remember_me = BooleanField('Remember me', default = False)
    
class ReportForm(Form):
    categ1 = SelectField(u'categ', coerce=int)
    skills1 = SelectField()
    categ2 = SelectField()
    skills2 = SelectField()
    categ3 = SelectField()
    skill3 = SelectField()
    
class ExistingUser(object):
    def __init__(self, message="Email doesn't exists"):
        self.message = message

    def __call__(self, form, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError(self.message)

reset_rules = [validators.Required(),
          validators.Email(),
          ExistingUser(message='Email address is not available')
         ]

class ResetPassword(Form):
    email = TextField('Email', validators=reset_rules)

class ResetPasswordSubmit(Form):
    password = PasswordField('Password', validators=[Required(),validators.Length(max=100, message=(u'edit_password'))])
    confirm = PasswordField('Confirm Password')