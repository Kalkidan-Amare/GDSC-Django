import os
import django
from datetime import datetime
from BlogApp.models import Post
from CommentApp.models import Comment

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDSCBlog.settings")
django.setup()

def create_posts():
    Post.objects.create(title='Post 1', content='Content 1', category='Category 1', tags=['Tag1', 'Tag2'])
    Post.objects.create(title='Post 2', content='Content 2', category='Category 2', tags=['Tag3', 'Tag4'])
    Post.objects.create(title='Post 3', content='Content 3', category='Category 1', tags=['Tag5', 'Tag6'])

def query_posts_in_category(category_name):
    posts = Post.objects.filter(category=category_name)
    for post in posts:
        print(f'Title: {post.title}, Category: {post.category}, Content: {post.content}, Tags: {post.tags}')

def update_post_content(post_id, new_content):
    post = Post.objects.get(pk=post_id)
    post.content = new_content
    post.save()

def delete_post(post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()

def create_comments():
    post1 = Post.objects.get(title='Post 1')
    post2 = Post.objects.get(title='Post 2')
    post3 = Post.objects.get(title='Post 3')

    Comment.objects.create(content='Comment 1 for Post 1', author='User1', published_date=datetime.now(), post=post1)
    Comment.objects.create(content='Comment 2 for Post 2', author='User2', published_date=datetime.now(), post=post2)
    Comment.objects.create(content='Comment 3 for Post 3', author='User3', published_date=datetime.now(), post=post3)

def query_comments_for_post(post_id):
    comments = Comment.objects.filter(post__id=post_id)
    for comment in comments:
        print(f'Comment for Post {post_id}: {comment.content}, Author: {comment.author}, Date: {comment.published_date}')

def update_comment_content(comment_id, new_content):
    comment = Comment.objects.get(pk=comment_id)
    comment.content = new_content
    comment.save()

def delete_comment(comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()

if __name__ == '__main__':
    create_posts()
    query_posts_in_category('Category 1')
    update_post_content(1, 'New content for Post 1')
    delete_post(2)
    create_comments()
    query_comments_for_post(1)
    update_comment_content(1, 'Updated comment for Post 1')
    delete_comment(2)
