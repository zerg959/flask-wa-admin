from blog import app
from blog.main.routes import main

app.register_blueprint(main)

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
