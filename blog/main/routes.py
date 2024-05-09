from flask import (
    render_template, request,
    flash, url_for, Blueprint,
    redirect
    )

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index1.html')
