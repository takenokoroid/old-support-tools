from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object("flaskApp.config.Config")
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    services = db.relationship('Service')
    def __init__(self, name):
        self.name = name

class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String, nullable=True)
    deleted = db.Column(db.Boolean, nullable=False, )

    def __init__(self, name, user_id, role):
        self.name = name
        self.user_id = user_id
        self.role = role
        self.deleted = False


@app.route("/")
def hello_world():
    return render_template("index.html")