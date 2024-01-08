from django.urls import path
from .views import (
    landing,
    home,
    new_topic,
    individual_topic,
    delete_topic,
    new_entry,
    individual_entry,
    edit_entry,
    delete_entry
)

app_name = 'learning_log'

# URLs for the the learning log app
urlpatterns = [
    path('', landing, name='landing'),
    path('topics/all/', home, name='home'),
    path('topics/new/', new_topic, name='new_topic'),
    path('topics/<int:topic_id>/', individual_topic, name='individual_topic'),
    path('topics/<int:topic_id>/delete/', delete_topic, name='delete_topic'),
    path('entries/new/<int:topic_id>/', new_entry, name='new_entry'),
    path('entries/<int:entry_id>/', individual_entry, name='individual_entry'),
    path('entries/<int:entry_id>/edit/', edit_entry, name='edit_entry'),
    path('entries/<int:entry_id>/delete/', delete_entry, name='delete_entry'),
]
