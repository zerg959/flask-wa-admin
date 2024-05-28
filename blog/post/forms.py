from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Post title', validators=[DataRequired()])
    content = TextAreaField('Post content', validators=[DataRequired()])
    # picture = FileField('Post image (png, jpg)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Publish')


class PostUpdateForm(FlaskForm):
    title = StringField('Post title', validators=[DataRequired()])
    content = TextAreaField('Post content', validators=[DataRequired()])
    # picture = FileField('Post image (png, jpg)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Publish')
