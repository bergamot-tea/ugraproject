from django.contrib import admin

# Register your models here.

from .models import Issue, Message

admin.site.register(Issue)
admin.site.register(Message)