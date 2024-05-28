from flask import Flask, render_template, url_for
from flask_admin import Admin, expose, AdminIndexView, BaseView
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, current_user


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Log In to view this content'

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()


class DashBoardView(AdminIndexView):
    @login_required
    @expose('/')
    def admin_panel(self):
        from blog.models import MyUser
        all_users = MyUser.query.all()
        # image_file = url_for('static',
        #                      filename=f'profile_pics' + '/users/' + current_user.username + '/account_img/' +
        #                               current_user.image_file)
        return self.render('admin/index_admin1.html', all_users=all_users) # , image_file=image_file)



class AnyPageView(BaseView):
    @expose('/')
    def any_page(self):
        return self.render('main/index.html')


# class MyModelView(ModelView):
#     def is_accsessiblr(self):
#         return current_user.is_authenticated

admin = Admin(name='Admin Board', template_mode='bootstrap3', index_view=DashBoardView(), endpoint='admin')

def create_app():
    app = Flask(__name__)
    # admin = Admin(app, name='Admin Board')
    admin.init_app(app)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from blog.models import MyUser, MyPost # Comment, Tag

    admin.add_view(AnyPageView(name='На блог'))
    admin.add_view(ModelView(MyUser, db.session, name='User name'))
    admin.add_view(ModelView(MyPost, db.session, name='User Posts'))
    # admin.add_view(ModelView(MyComment, db.session, name='Комментарии'))
    # admin.add_view(ModelView(Tag, db.session, name='Теги'))

    from blog.main.routes import main
    from blog.user.routes import users
    from blog.post.routes import posts


    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    return app
