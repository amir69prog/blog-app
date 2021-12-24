from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
	path('', BlogListView.as_view(), name='list'),
	path('post/<pk>', BlogDetailView.as_view(), name='detail'),
	path('post/new/', BlogCreateView.as_view(), name='post_new'),
	path('post/edit/<pk>', BlogUpdateView.as_view(), name='post_edit'),
	path('post/delete/<pk>', BlogDeleteView.as_view(), name='post_delete'),
] 