
import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post
from app_comments.forms import CommentForm

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post':post,
    			'form': form,
    			'comment_list': comment_list
    			}
    return render(request, 'app_blog/detail.html', context=context)