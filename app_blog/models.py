# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=70)
	body = RichTextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200, blank=True) #文章摘要，内容可以为空

	# 这是分类与标签，
    # 分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类与标签对应的表关联起来，
    # 但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，
    # 但是一个分类下可以有很多篇文章，
    # 所以我们使用的是 ForeignKey，
    # 即一对多的关系。
    # 而对于标签来说，
    # 一篇文章可以有多个标签，
    # 同一个标签下也可能有多篇文章，
    # 所以我们使用 ManyToManyField，
    # 表明这是多对多的关系。
    # 同时我们规定文章可以没有标签，
    # 因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，
    # 请看教程中的解释，
    # 亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User)
	
	def __str__(self):
		return self.title

	#自定义get_absolute_url方法
	def get_absolute_url(self):
		return reverse('app_blog:detail', kwargs={'pk':self.pk})
		#注意到 URL 配置中 url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail') ，
		#我们设定、的 name='detail'，这里派上了用场。看到这个 reverse 函数，
		#它的第一个参数的值是 'blog:detail'，
		#意思是 app_blog 应用下的 name=detail 函数，
		#由于我们在上面通过 app_name = 'app_blog' 告诉了 django 这个 URL 模块是属于 blog 应用的，
		#因此 django 能够顺利地找到 blog 应用下 name 为 detail 的视图函数，
		#于是 django 会去解析这个视图函数对应的 url，
		#我们这里 detail 对应的规则就是 post/(?P<pk>[0-9]+)/ 这个正则表达式规则，
		#而正则表达式部分会被后面传入的参数 pk 替换，所以，如果 post 的 id 是 255 的话，
		#那么 get_absolute_url 函数返回的就是 /post/255/ ，这样 Post 自己就生成了自己的 url。

	class Meta:
		ordering = ['-created_time','title']
		
