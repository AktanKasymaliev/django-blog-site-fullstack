from django.test import TestCase
from django.utils import timezone
# from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.db.utils import IntegrityError

from customUsers.models import User
from blogs.models import Post, Comments



class BaseTestCase(TestCase):

    def setUp(self) -> None:
        self.register_url = reverse('signup')
        self.user = {"email": "test1@gmail.com", "username": "test1",
                "password": "password", "password2": "password"}

        self.user_short_pass = {"email": "test2@gmail.com", "username": "test2",
                "password": "pass", "password2": "passw"}

        self.user_unmatching_passwords = {"email": "test3@gmail.com", "username": "test3",
                "password": "password", "password2": "password123"}

        self.created_user = User.objects.create(email='test@mail.ru', username='username_test',
                                                password='password')
        self.post = Post.objects.create(
            title='Test', owner=self.created_user,
            created_at=timezone.now(), text='test text',
            tag='test')
        self.comment = Comments.objects.create(
            author=self.created_user, sent_at=timezone.now(),
            message='test text', post=self.post)

class RegisterTestCase(BaseTestCase):

    def test_can_register_user(self):
        response = self.client.post(self.register_url, data=self.user)
        self.assertEqual(response.status_code, 302)
    
    def test_cant_register_with_shortpass(self):
        try:
            response = self.client.post(self.register_url, self.user_short_pass)
            self.assertEqual(response.status_code, 400)
            return False
        except KeyError:
            return True
    
    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(self.register_url, self.user_unmatching_passwords)
        self.assertEqual(response.status_code, 400)
    
    def test_cant_register_withtaken_email(self):
        self.client.post(self.register_url, self.user)
        try:
            response = self.client.post(self.register_url, self.user)
            self.assertEqual(response.status_code, 400)
            return True
        except IntegrityError:
            return False