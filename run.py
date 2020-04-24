# -*- coding:utf-8 -*-


import os
from flask import Flask, render_template, request, redirect, flash
from models import *
from forms import SignUp, SignIn
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)

@app.route('/')
def index():
    '''
    처음 사이트에 들어왔을 때 보여지는 메인 홈
    '''
    return render_template('index.html')


@app.route('/sign_in', methods=['GET', "POST"])
def sign_in():
    '''
    로그인 화면
    '''
    sign_in_form = SignIn()
    if sign_in_form.validate_on_submit():
        inputEmail = sign_in_form.data.get("inputEmail")
        inputPassword = sign_in_form.data.get("inputPassword")
        print(inputEmail, inputPassword)

        return redirect("/")
    return render_template('sign_in.html', sign_in_form=sign_in_form)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    '''
    회원가입 화면
    '''
    sign_up_form = SignUp()
    if sign_up_form.validate_on_submit():
        inputName = sign_up_form.data.get("inputName")
        inputEmail = sign_up_form.data.get("inputEmail")
        inputPassword = sign_up_form.data.get("inputPassword")
        inputPhone = sign_up_form.data.get("inputPhone")

        email_check = db.session.query(User).filter(User.email == inputEmail).first()
        if email_check is None:
            user = User()
            user.name = inputName
            user.email = inputEmail
            user.password = inputPassword
            user.phone = inputPhone
            db.session.add(user)
            db.session.commit()
            return redirect("/")
        else:
            flash("중복된 이메일입니다.", "email_error")

    return render_template('sign_up.html', sign_up_form=sign_up_form)


if __name__ == "__main__":
    # 현재 파일이 있는 절대 경로 반환
    basedir = os.path.abspath(os.path.dirname(__file__))
    # basedir 경로에 db.sqlite 라는 데이터베이스 생성
    dbfile = os.path.join(basedir, 'db.sqlite')

    # flask에서 사용할 데이터베이스의 경로 설정 sqlite3는 sqlite:/// 시작
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    # SQLALCHEMY_COMMIT_ON_TEARDOWN : app경로 이용 시 자동 commit
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # 추가적인 메모리 사용 방지를 위해 False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'This is Secret key'

    csrf = CsrfProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port='5000', debug=True)










