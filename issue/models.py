from django.db import models
from project.models import Project
from django.contrib.auth.models import User

# Create your models here.


class Issue(models.Model):
    STATUS = (
    (1, 'Открыта'),
    (2, 'В работе'),
    (3, 'Закрыта'),
    )

    project = models.ForeignKey(Project, on_delete=models.SET('проект удален'))
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    date_open = models.DateField(auto_now_add=True, blank=True)
    date_change = models.DateField(auto_now=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET('пользователь удален'))
    status = models.IntegerField(default=1, choices=STATUS, blank=True)
    file1 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)


class Message(models.Model):
    id_issue = models.ForeignKey(Issue, on_delete=models.SET('заявка удалена'))
    author = models.ForeignKey(User, on_delete=models.SET('пользователь удален'))
    date_post = models.DateField(auto_now_add=True, blank=True)
    text = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='screens/%Y/%m/%d', blank=True)
    file1 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
