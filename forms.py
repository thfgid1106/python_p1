from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class SignUp(FlaskForm):
    inputName = StringField("inputName", validators=[DataRequired()])
    inputEmail = StringField("inputEmail", validators=[DataRequired()])
    inputPassword = PasswordField("inputPassword", validators=[DataRequired(), EqualTo("inputPasswordCheck")])
    inputPasswordCheck = PasswordField("inputPasswordCheck", validators=[DataRequired()])
    inputPhone = StringField("inputPhone", validators=[DataRequired()])


class SignIn(FlaskForm):
    inputEmail = StringField("inputEmail", validators=[DataRequired()])
    inputPassword = PasswordField("inputPassword", validators=[DataRequired()])
