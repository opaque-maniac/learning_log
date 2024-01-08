from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Topic, Entry

# Test for the topic and entry model
class TopicEntryModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            email='user@test.com',
            first_name='user first',
            last_name='user last',
            password='foobaar'
        )
        test_user.save()
        test_topic = Topic.objects.create(
            text='Chess',
            author=test_user
        )
        test_topic.save()
        test_entry = Entry.objects.create(
            text='I learned the different pieces of the chess board',
            topic=test_topic
        )
        test_entry.save()
    
    # Test for the topic model
    def test_topic_model(self):
        user = get_user_model().objects.get(id=1)
        topic = Topic.objects.get(id=1)
        self.assertIsNotNone(user)
        self.assertIsNotNone(topic)
        self.assertEqual(topic.text, 'Chess')
        self.assertEqual(topic.author, user)

    # Test for the entry model
    def test_entry_model(self):
        user = get_user_model().objects.get(id=1)
        topic = Topic.objects.get(id=1)
        entry = Entry.objects.get(id=1)
        self.assertIsNotNone(user)
        self.assertIsNotNone(topic)
        self.assertIsNotNone(entry)
        self.assertEqual(entry.text, 'I learned the different pieces of the chess board')
        self.assertEqual(entry.topic, topic)
    
    # Test string representation for the topic model
    def test_topic_string_representation(self):
        user = get_user_model().objects.get(id=1)
        topic = Topic.objects.create(
            text='Cooking',
            author=user
        )
        self.assertEqual(str(topic), "Cooking")
    
    # Test string representation for the entry model
    def test_entry_string_representation(self):
        topic = Topic.objects.get(id=1)
        entry_text = "I learned about how the different pieces are allowed to move"
        entry = Entry.objects.create(
            text=entry_text,
            topic=topic
        )
        self.assertEqual(str(entry), entry_text[:50])

# Test for the landing page view
class LandingPageViewTest(TestCase):
    def test_response_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('learning_log:landing'))
        self.assertEqual(response.status_code, 200)
    
    def test_response_templates(self):
        response = self.client.get(reverse('learning_log:landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('header.html')
        self.assertTemplateUsed('footer.html')
        self.assertTemplateUsed('base.html')
        self.assertTemplateUsed('learning_log/landing.html')

# Test for the home page view
class HomePageViewTest(TestCase):
    def test_response_code(self):
        response = self.client.get('/topics/all/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('learning_log:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_response_templates(self):
        response = self.client.get(reverse('learning_log:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('header.html')
        self.assertTemplateUsed('footer.html')
        self.assertTemplateUsed('base.html')
        self.assertTemplateUsed('learning_log/home.html')

# Test for the new topic page view
class NewTopicPageViewTest(TestCase):
    def test_response_code(self):
        response = self.client.get('/topics/new/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_code_name(self):
        response = self.client.get(reverse('learning_log:new_topic'))
        self.assertEqual(response.status_code, 200)

    def test_response_templates(self):
        response = self.client.get(reverse('learning_log:new_topic'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('header.html')
        self.assertTemplateUsed('footer.html')
        self.assertTemplateUsed('base.html')
        self.assertTemplateUsed('learning_log/new_topic.html')

