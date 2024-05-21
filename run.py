from blog import app
from blog.main.routes import main
from flask_login import LoginManager

app.register_blueprint(main)
app.config.from_pyfile('main/settings.py')

# login_manager = LoginManager()
# login_manager.login_view = 'main.login'
# login_manager.login_message_category = 'danger'
# login_manager.init_app(app)
if __name__ == '__main__':
    app.run(debug=True, port=5000)

















# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index1.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/register')
# def about():
#     return render_template('register.html')


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
