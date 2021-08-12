from flask_wtf import Form, FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')

    @staticmethod
    def validate_username(username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please, use a different username.')

    @staticmethod
    def validate_email(email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please, use a different email address.')
