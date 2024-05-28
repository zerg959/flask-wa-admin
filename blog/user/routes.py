import os
import shutil

from flask import (
    render_template, request,
    flash, url_for, Blueprint,
    redirect
    )
from flask_login import login_user, current_user, login_required, logout_user

from blog import bcrypt, db
from blog.models import MyUser, MyPost
from blog.user.forms import RegistrationForm, LoginForm


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.blog'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = MyUser(username=form.username.data, email=form.email.data, password=hashed_password, role=form.role.data)
        db.session.add(user)
        db.session.commit()

        full_path = os.path.join(os.getcwd(), 'blog/static', 'profile_pics', user.username)
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        shutil.copy(f'{os.getcwd()}/blog/static/profile_pics/default.png', full_path)
        flash('Account succefully created. Please, login', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form_registration=form, title='Registration Form', legend='Registration Form')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = MyUser.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                                form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'You are logged in as {current_user.username}', 'success')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('Login failed. Please, check email and/or password', 'danger')
    return render_template('login.html', form_login=form, title='login', legend="Login")

@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    user=current_user
    # user = MyUser.query.filter_by(username=current_user.username).first()
    return render_template('account1.html', title='account1', user=current_user)


@users.route('/logout')
def logout():
    logout_user()
    flash('You are logged out successfully!', 'success')
    return redirect(url_for('users.login'))


@users.route('/user/<string:username>')
# @users.route('/blog')
@login_required
def user_posts(username):
    # page =  request.args.get('page', 1 , type=int)
    user = MyUser.query.filter_by(username=username).first_or_404()
    posts = MyPost.query.filter_by(user_id=user.id).order_by(MyPost.date_posted.desc())  #.paginate(page=page, per_page=5)
    return render_template('blog.html', title='Blog', user=user, posts=posts) 
  # Доделать редирект на блог пользователя
