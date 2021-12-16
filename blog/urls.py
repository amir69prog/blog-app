from django.urls import path

from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
	path('', BlogListView.as_view(), name='list'),
	path('post/<pk>', BlogDetailView.as_view(), name='detail')
] 