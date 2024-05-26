import os
import shutil

from flask import (
    render_template, request,
    flash, url_for, Blueprint,
    redirect
    )
from flask_login import login_user, current_user, login_required, logout_user

from blog import bcrypt, db
from blog.models import User
from blog.user.forms import RegistrationForm, LoginForm


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form_registration = RegistrationForm()
    if form_registration.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form_registration.password.data).decode('utf-8')
        user = User(username=form_registration.username.data, email=form_registration.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        full_path = os.path.join(os.getcwd(), 'blog/static/img', 'profile_pics', user.username)
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        shutil.copy(f'{os.getcwd()}/blog/static/img/profile_pics/default.png', full_path)
        flash('Account succefully created. Please, login', 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', form_registration=form_registration, title='Registration Form', legend='Registration Form')

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('Войти не удалось. Пожалуйста, проверьте электронную почту или пароль', 'danger')
    return render_template('login1.html', title='login1', legend="Login", form=form)


@users.route('/account')
@login_required
def account():
    return render_template(
        'account1.html',
        title='account1',
        current_user=current_user)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))