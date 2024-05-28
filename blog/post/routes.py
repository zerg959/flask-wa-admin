from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import current_user, login_required

from blog import db
from blog.models import MyPost
from blog.post.forms import PostForm
# from blog.post.utils import save_picture_post


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods= ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = MyPost(
            title=form.title.data,
            content=form.content.data,
            # image_post=form.picture.data,
            author=current_user)
        # picture_file = save_picture_post(form.picture.data)
        # post.image_post = picture_file
        db.session.add(post)
        db.session.commit()
        flash('Post published successfully!', 'success')
        return redirect(url_for('main.index'))
    # image_file = url_for('static',
    #                      filename=f'profile_pics/' + current_user.username + '/post_images/' + current_user.image_file)
    return render_template('create_post.html', title='New Post', form=form, legend='New Post') # image_file=image_file)


@posts.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = MyPost.query.get_or_404(post_id)
    # image_file = url_for('static',
    #                      filename=f'profile_pics/' + post.author.username + '/post_images/' + post.image_post)
    return render_template('post.html', title=post.title, post=post)  #  image_file=image_file
