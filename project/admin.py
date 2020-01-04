from django.contrib import admin

# Register your models here.
from .models import Project, Member, Report, Chat

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Report)
admin.site.register(Chat)