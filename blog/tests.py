from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTest(TestCase) :
    def Setup(self):
        Post.objects.create(
            title='myTitle',
            body='just a test'
        )

    def test_string_representation(self):
        article = Post(title='My entry title')
        self.assertEqual(str(article), article.title)

    def test_post_list_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
        self.assertContains(response, 'Blog')

    def test_post_list_view(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article.html')
        self.assertContains(response, 'Blog')
