from django.db import models

# Create your models here.



class Member(models.Model):

    fio = models.CharField(max_length=255)
    fio_full = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tell = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255)


class Project(models.Model):

    PORTFOLIOS = (
        ('1','Демография'),
        ('2','Здравоохранение'),
        ('3','Образование'),
        ('4','Жилье и городская среда'),
        ('5','Безопасные и качественные автомобильные дороги'),
        ('6','Цифровая экономика'),
        ('7','Международная кооперация и экспорт'),
        ('8','Производительность труда и поддержка занятости'),
        ('9','Малое и среднее предпринимательство'),
        ('10','Экология'),
        ('11','Культура'),
    )

    ANSWER = (
        ('1','Да'),
        ('2','Нет'),
        ('3','Неизвестно'),

    )

    name = models.CharField(max_length=255)
    portfolio = models.CharField(max_length=4)
    code = models.CharField(max_length=3)
    date_change_status = models.DateField()
    comment = models.CharField(max_length=255)
    administrator = models.CharField(max_length=30)
    critical_error = models.CharField(max_length=30)
    curator = models.CharField(max_length=30)


