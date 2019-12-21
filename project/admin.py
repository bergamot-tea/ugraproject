from django.contrib import admin

# Register your models here.
from .models import Project, Member

admin.site.register(Project)
admin.site.register(Member)