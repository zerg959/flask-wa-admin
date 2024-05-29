from flask import Flask, render_template, url_for
from flask_admin import Admin, expose, AdminIndexView, BaseView
# from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, current_user

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Log In to view this content'

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()


class UserModelView(ModelView):
    column_list = ('username', 'email')
    form_columns = ('username', 'email')


def create_app():
    from blog.models import MyUser, MyPost
    app = Flask(__name__)
    # admin = Admin(app)
    admin = Admin(app, name='Admin Board', template_mode='bootstrap3')
    admin.add_view(UserModelView(MyUser, db.session, name='Users'))
    admin.add_view(ModelView(MyPost, db.session, name='Posts'))
    # admin.init_app(app)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

 # Comment, Tag
    from blog.main.routes import main
    from blog.user.routes import users
    from blog.post.routes import posts


    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    return app
