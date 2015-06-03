from flask.ext.mail import Message
import os
from application import app, mail

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='trill@landregistry.gsi.gov.uk'
    )
    print (msg)
    mail.send(msg)