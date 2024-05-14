from flask import (
    render_template, request,
    flash, url_for, Blueprint,
    redirect
    )
from blog.main.forms import LoginForm
from blog.models import User
from blog.models import check_password_hash
from flask_login import login_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index1.html', title='index1')


@main.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.rememer.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.account'))
        else:
            flash('Войти не удалось. Пожалуйста, проверьте электронную почту или пароль', 'danger')
    return render_template('login1.html', title='login1', legend="Login", form=form)


@main.route('/account')
def account():
    return render_template('account1.html', title='account1')


@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))
