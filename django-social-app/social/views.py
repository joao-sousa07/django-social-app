from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'social/home.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'social/post_detail.html', {'post': post})

def user_posts(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)

    return render(request, 'social/user_posts.html', {
        'posts': posts,
        'user_profile': user
    })