from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# db = SQLAlchemy(app)
db = SQLAlchemy()

bcrypt = Bcrypt()
