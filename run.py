# -*- coding:utf-8 -*-

import os
from flask import Flask, render_template
from models import db



app = Flask(__name__)


@app.route('/a')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbflie = os.path.join(basedir, 'test.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbflie
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host="127.0.0.1", port = '5000', debug=True)




