import unittest
from app.models import Post, User
from flask_login import current_user

class TestUser(unittest.TestCase):
    '''
        Test Class to test the behaviour of the db
      '''

    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.user = User(username='dummy', email="dummytest@gmail.com", password="password")

    def tearDown(self):
        self.user = None


    def test_post_model(self):
        post = Post(title="new blog post",content = "This is a new blog post",
                    category= "Entertainment", summary ="blog post summary",
                    image_file = "default.jpg", author=self.user)
        self.assertEqual('Entertainment',post.category)