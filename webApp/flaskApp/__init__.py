from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object("flaskApp.config.Config")
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True,
                   unique=True, autoincrement=True)
    cgg_id = db.Column(db.String, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    services = db.relationship('Service')

    def __init__(self, cgg_id, name):
        self.cgg_id = cgg_id
        self.name = name


class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True,
                   unique=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    deleted = db.Column(db.Boolean, nullable=False, )

    def __init__(self, user_id, deleted):
        self.user_id = user_id
        self.deleted = deleted


@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        result = {}
        cgg_id = request.form["userid"]

        user = Users.query.filter_by(cgg_id=cgg_id).first()
        if user is None:
            return render_template("index.html", result=result)

        service = Service.query.filter_by(user_id=user.__dict__["id"]).first()
        if service is None:
            return render_template("index.html", result=result)

        result = {
            "user": {
                "cgg_id": user.__dict__["cgg_id"],
                "name": user.__dict__["name"]
            },
            "service": {
                "deleted": service.__dict__["deleted"]
            }
        }
        return render_template("index.html", result=result)
    else:
        return render_template("index.html")
