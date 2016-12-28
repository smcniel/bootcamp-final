from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
# You can ignore this line if you want to. It suppresses a warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your database table as a Python class.
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mes_id = db.Column(db.String(10))
    subject = db.Column(db.String(80))
    recipient = db.Column(db.String(40))
    sender = db.Column(db.String(40))
    date = db.Column(db.DateTime)
    email_body = db.Column(db.String)

    def __init__(self, mes_id, subject, recipient, sender, date, email_body):
        self.mes_id = mes_id
        self.subject = subject
        self.recipient = recipient
        self.sender = sender
        self.date = date
        self.email_body = email_body
