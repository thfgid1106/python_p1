# -*- coding:utf-8 -*-

import os
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index2.html")


@app.route('/information', methods=['POST'])
def information():
    username = request.form["username"]
    birth = request.form["birth"]
    major = request.form["major"]
    return render_template("action.html", username=username, birth=birth, major=major)


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbflie = os.path.join(basedir, 'test.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbflie
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    with app.app_context():
        db.create_all()

    app.run(host="127.0.0.1", port='7000', debug=True)
