from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def news_view(request):
    posts = Post.objects.all()
    data = {'posts': posts}
    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    data = {'post': post}
    return render(request, 'post_detail.html', data)
