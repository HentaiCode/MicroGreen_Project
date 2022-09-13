from flask import render_template, redirect, Blueprint
from flask_login import login_user, login_required, logout_user

from forms.user import RegisterForm, LoginForm
from database.repositories import users_rep
from database.models.users import User


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/MicroGreen")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        users_rep.save_user(user, form.password.data)

        return redirect('/user/login')
    return render_template('register.html', title='Регистрация', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users_rep.get_user_by_email(form.email.data)
        login_user(user, remember=form.remember_me.data)
        return redirect("/MicroGreen")
    return render_template('login.html', title='Авторизация', form=form)
