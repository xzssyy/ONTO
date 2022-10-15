from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    # 按序验证
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)], render_kw={'type': "email",
                                                                                        'class': "form-control",
                                                                                        'id': "exampleInputEmail1",
                                                                                        })
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'type': "password",
                                                                                 'class': "form-control"})
    remember_me = BooleanField('Keep me logged in', render_kw={'class': "form-check-input"})
    submit = SubmitField('Log In')


class UploadForm(FlaskForm):
    name = StringField()


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()], render_kw={"type": "email",
                                                                                                 "class": "form-control",
                                                                                                 "id": "exampleInputEmail1",
                                                                                                 "placeholder": "Please fill in the email form."})

    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名只能含有字母或数字或.或_')
    ], render_kw={'type': "text",
                  'class': "form-control",
                  'placeholder': "Enter Email"})

    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='请一致的密码')],
                             render_kw={'type': "assword",
                                        'class': "form-control",
                                        'placeholder': "Please enter a password."})

    password2 = PasswordField('Confirm password', validators=[DataRequired()], render_kw={'type': "assword",
                                                                                          'class': "form-control",
                                                                                          'placeholder': "Please enter a password."})

    submit = SubmitField('注册', render_kw={'class': "btn-action"})

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('邮箱已注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')
