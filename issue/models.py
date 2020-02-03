from django.db import models
from project.models import Project
from django.contrib.auth.models import User


# Create your models here.


class Issue(models.Model):
    STATUS = (
    (0, 'Открыта'),
    (1, 'Закрыта'),
    )

    project = models.ForeignKey(Project, on_delete=models.SET('проект удален'))
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    time_open = models.DateTimeField(auto_now_add=True, blank=True)
    time_change = models.DateTimeField(auto_now=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET('пользователь удален'))
    status = models.IntegerField(default=0, choices=STATUS, blank=True)
    file1 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file2 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file3 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)


class Message(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.SET('заявка удалена'))
    author = models.ForeignKey(User, on_delete=models.SET('пользователь удален'))
    time = models.DateTimeField(auto_now_add=True, blank=True)
    time_change = models.DateTimeField(auto_now=True, blank=True)
    text = models.TextField(blank=True)
    file1 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file2 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file3 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)