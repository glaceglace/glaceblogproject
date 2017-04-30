
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
import markdown

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'app_blog/index.html', context={'post_list': post_list})

def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
	return render(request, 'app_blog/detail.html', context={'post':post})

def archives(request, year, month):
	post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
	return render(request, 'app_blog/index.html', context={'post_list': post_list})

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Post.objects.filter(category=cate)
	return render(request, 'app_blog/index.html', context={'post_list':post_list})
