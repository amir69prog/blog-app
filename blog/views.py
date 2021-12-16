from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'post_list'


class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'
