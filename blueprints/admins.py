from flask import render_template, redirect, Blueprint
from flask_login import login_user, login_required, logout_user

from forms.admin import RegisterForm, LoginForm
from database.repositories import admins_rep
from database.models.admins import Admin


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        admin = Admin()
        form.populate_obj(admin)
        admins_rep.save_admin(admin, form.password.data)

        return redirect('/MicroGreen')
    return render_template('register.html', title='Регистрация', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = admins_rep.get_admin_by_email(form.email.data)
        login_user(admin, remember=form.remember_me.data)
        return redirect("/MicroGreen")
    return render_template('login.html', title='Авторизация', form=form)
