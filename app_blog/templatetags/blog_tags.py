from ..models import Post, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all()[:num]#侧边栏的最近发表

@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order='DESC')#归档

@register.simple_tag
def get_categories():
	return Category.objects.all()#分类