from flask.cli import FlaskGroup

from flaskApp import app, db
from flaskApp import Users, Service


cli = FlaskGroup(app)


def init():
    # User 1
    user = Users(cgg_id="GL1004", name="ジル")
    db.session.add(user)
    db.session.flush()
    service = Service(user_id=user.id, deleted=False)
    db.session.add(service)
    # User 2
    user = Users(cgg_id="LP0006", name="シィル・プライン")
    db.session.add(user)
    db.session.flush()
    service = Service(user_id=user.id, deleted=True)
    db.session.add(service)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    init()
    db.session.commit()

# @cli.command("seed_db")
# def seed_db():
#     db.session.add(User(email="michael@mherman.org"))
#     db.session.commit()


if __name__ == "__main__":
    cli()
