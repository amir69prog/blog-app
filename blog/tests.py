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

	def test_get_absolute_url(self):
		self.assertEqual(self.post.get_absolute_url(), '/post/1')
	


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

	def test_post_create(self):
		payload = {
			'title':'New title',
			'body':'New body',
			'author':self.user.id
		}
		response = self.client.post(reverse('blog:post_new'), data=payload)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(Post.objects.last().title, 'New title')
		self.assertEqual(Post.objects.last().body, 'New body')

	def test_post_update(self):
		payload = {
			'title':'New title Updated',
			'body':'New body Updated'
		}
		response = self.client.post(reverse('blog:post_edit', args=[1]), payload)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(Post.objects.last().title, 'New title Updated')
		self.assertEqual(Post.objects.last().body, 'New body Updated')

	def test_post_delete(self):
		response = self.client.post(reverse('blog:post_delete', args=[1]))
		self.assertEqual(response.status_code, 302)
		