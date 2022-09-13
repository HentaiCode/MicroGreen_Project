import wtforms
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, EqualTo
from .validators import EmailUnique, Password


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), EmailUnique(message='Такой mail уже существует!')])
    password = PasswordField('Пароль',
                             validators=[DataRequired(), EqualTo('password_again', message='Пароли не совпадают!')])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    username = StringField('Придумай эпичный ник, чтоб простые смертные аж обосрались', validators=[DataRequired()])
    position = wtforms.SelectField(label='Насколько же ты бессмртен',
                                   choices=['Гл. админ', 'Товаровед', 'Разработчик'])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Password('Неправильный логин или пароль')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
