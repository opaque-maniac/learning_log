from django.contrib import admin
from .models import Topic, Entry

# Registering models
admin.site.register(Topic)
admin.site.register(Entry)
