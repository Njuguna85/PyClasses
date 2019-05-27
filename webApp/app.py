import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
#   SQLAlchemy is a database management library based on psycopg2
from sqlalchemy.sql import func

app = Flask(__name__)
#   creating our app under the name 'app'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123456789@localhost/height_collector'
#   configuring the dbase uri to its dbase adapter://user:pwd@host/dbaseName

db = SQLAlchemy(app)
#    creating a SQLAlchemy object for the app


class Data(db.Model):
    __tablename__ = "Heights"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Float)

    def __init__(self, email, height):
        self.email = email
        self.height = height

    def __repr__(self):
        return '<id{}>'.format(self.id)

#   Table definition with its field.
#   After its definition; run python from the terminall
#   and from app import db
#  then run db.create_all() to create them in the dbase


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/name/<name>")
def get_my_name(name):
    return "My name is: {}".format(name)


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        height = request.form['height']
        #   fecthing the input variables if a post was done

        if db.session.query(Data).filter(Data.email == email).count() == 0:

            data = Data(email, height)
            #   we pass them as objects to the Data Class of database
            db.session.add(data)
            db.session.commit()
            # and finally add and commit the changes

            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count)

            return render_template("success.html")
        return render_template('index.html',
                               text="The Email submitted has had an entry earlier")


if __name__ == "__main__":
    app.debug = True
    app.run()
