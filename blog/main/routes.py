from flask import (
    render_template, request,
    flash, url_for, Blueprint,
    redirect
    )
from blog.main.forms import LoginForm
from blog.models import User
from blog.models import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', title='Main Page')

@main.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')



