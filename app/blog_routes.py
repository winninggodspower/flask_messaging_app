from flask import redirect,url_for,render_template, flash, request
from flask_login import login_user, logout_user, current_user, login_required
import json

from app import app, db
from app.forms import BlogForm
from app.models import Post, Like

@app.route('/post/new', methods=["POST","GET"])
@login_required
def new_post():
    form = BlogForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data,
                    text = form.content.data,
                    user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('successfully posted a blog', 'success')
        return redirect('/')
    return render_template('new_post.html', form=form)


@app.route('/get_posts' ,methods=['GET'])
def get_posts():
    offset = int(request.args.get('offset'))
    posts = db.view_data()[ offset: offset + 10]

    return render_template('partial/post.html', posts = posts, offset = offset + 10)


""" route to delete post"""
@app.route('/post/delete/<string:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    if current_user == post.user:
        db.session.delete(post)
        db.session.commit()
    
    return redirect('/')
    # '''simply redirecting back to the main page'''


@app.route('/post/edit/<string:id>' ,methods=['GET','POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)

    if current_user.id != post.user_id:
        flash("you don't have permission to edit this post", "danger")
        return redirect("/")

    form = BlogForm(title=post.title, content=post.text)

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.content.data
        db.session.add(post)
        db.session.commit()
        flash('successfully edited post', 'success')
        return redirect('/')

    return render_template('edit.html', form=form, post=post)

@app.route('/post/like/<int:id>' ,methods=['POST'])
def like_post(id):

    if not current_user.is_authenticated:
        return json.dumps({
            "message": "failure",
            "action": "redirect",
            "redirect_url": "/login"
        })

    post = Post.query.get_or_404(id)

    if Like.query.filter_by(post_id=post.id, user_id=current_user.id).first():
        print("unlike")
        like = Like.query.filter_by(post_id=post.id, user_id=current_user.id).first()
        db.session.delete(like)
        db.session.commit()
        return json.dumps({
            "message": "success",
            "action": "unlike"
        })

    else:
        print("like")
        new_like = Like(post_id=post.id, user_id=current_user.id)
        db.session.add(new_like)
        db.session.commit()
        return json.dumps({
            "message": "success",
            "action": "like"
        })