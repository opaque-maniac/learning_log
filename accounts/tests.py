from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class TestCustomUserManager(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            email='user@test.com',
            first_name='user first',
            last_name='user last',
            password='foobar'
        )
        test_user.save()
        test_admin = get_user_model().objects.create_superuser(
            email='admin@test.com',
            first_name='admin first',
            last_name='admin last',
            password='foobar'
        )
        test_admin.save()

    # Test custom create user method
    def test_create_user(self):
        user = get_user_model().objects.get(id=1)
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'user@test.com')
        self.assertEqual(user.first_name, 'user first')
        self.assertEqual(user.last_name, 'user last')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    # Test custom create superuser method
    def test_create_superuser(self):
        admin = get_user_model().objects.get(id=2)
        self.assertIsNotNone(admin)
        self.assertEqual(admin.email, 'admin@test.com')
        self.assertEqual(admin.first_name, 'admin first')
        self.assertEqual(admin.last_name, 'admin last')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
    
    # Testing model string representation
    def test_string_representation(self):
        user = get_user_model().objects.create_user(
            email="onetwo@test.com",
            first_name="one",
            last_name="two",
            password="foobar"
        )
        self.assertEqual(str(user), "one two")

# Test for the register view
class TestRegisterView(TestCase):
    def test_response_code(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
    
    def test_response_templates(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'header.html')
        self.assertTemplateUsed(response, 'footer.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response,'accounts/register.html')
        self.assertTemplateNotUsed(response, 'accounts/login.html')
    
    def test_response_post_request(self):
        response = self.client.post(reverse('accounts:register'), {
            'email': 'user@test.com',
            'first_name': 'user first',
            'last_name': 'user last',
            'password': 'foobar'
        })
        self.assertEqual(response.status_code, 200)     
# Test for the login view
class RegisterViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            email='user@test.com',
            first_name='user first',
            last_name='user last',
            password='foobar'
        )
        test_user.save()

    def test_response_code(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
    
    def test_response_templates(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'header.html')
        self.assertTemplateUsed(response, 'footer.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response,'accounts/login.html')
        self.assertTemplateNotUsed(response, 'accounts/register.html')
    
    def test_response_post_request(self):
        response = self.client.post(reverse('accounts:register'), {
            'email': 'user@test.com',
            'password': 'foobar'
        })
        self.assertEqual(response.status_code, 200)
