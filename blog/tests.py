from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post



class PostModelTest(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='amirhossein',
			email='amirsacum@gmail.com',
		)
		self.user.set_password('amirhossein')

		self.post = Post.objects.create(
			author=self.user,
			title='Hello World!',
			body='Hello World is the most popular text for progremmers',
		)

	def test_string_representation(self):
		post = Post(title='Hello World!')
		self.assertEqual(str(post), post.title)

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'Hello World!')
		self.assertEqual(f'{self.post.body}', 'Hello World is the most popular text for progremmers')
		self.assertEqual(f'{self.post.author}', 'amirhossein')

	def test_post_list_view(self):
		response = self.client.get(reverse('blog:list'))
		self.assertEqual(response.status_code, 200) 
		self.assertContains(response, 'Hello World!')
		self.assertTemplateUsed(response, 'blog/post_list.html')

	def test_post_detail_view(self):
		response = self.client.get('/post/1')
		no_response = self.client.get('/post/40000')
		self.assertEqual(response.status_code, 200) 
		self.assertEqual(no_response.status_code, 404) 
		self.assertContains(response, 'Hello World is the most popular text for progremmers')
		self.assertTemplateUsed(response, 'blog/post_detail.html')