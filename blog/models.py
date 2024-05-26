from datetime import datetime, timezone

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin

from blog import db, bcrypt, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    posts = db.relationship('Post', backref='author', lazy=True)
    # role = db.Column(db.String(20), index=True)

    def set_password(self, password, hashed_password):
        self.hashed_password = bcrypt.generate_password_hash(
            password
            ).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
    # @property
    # def is_admin(self):
    #     return self.role == 'admin'

    def __repr__(self):
        return f'User({self.username}, {self.role}, {self.email}, {self.password}, {self.image_file})'


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    image_post = db.Column(db.String(30), nullable=True, default='none')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'User({self.title}, {self.date_posted}, {self.image_post})'