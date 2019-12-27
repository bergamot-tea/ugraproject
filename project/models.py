from django.db import models

# Create your models here.



class Member(models.Model):

    fio = models.CharField(max_length=255)
    job = models.CharField(max_length=255, blank=True)
    post = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    tell = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)


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
    portfolio = models.CharField(max_length=4, blank=True)
    code = models.CharField(max_length=4, blank=True)
    date_change_status = models.DateField(blank=True)
    comment = models.CharField(max_length=255, blank=True)
    administrator = models.CharField(max_length=30, blank=True)
    critical_error = models.CharField(max_length=30, blank=True)
    curator = models.CharField(max_length=30, blank=True)



class Report(models.Model):
    ANSWER = (
        (1,'Да'),
        (2,'Нет'),
        (3,'Неизвестно'),

    )

    MONTHS = (
        (1,'Январь'),
        (2,'Февраль'),
        (3,'Март'),
        (4,'Апрель'),
        (5,'Май'),
        (6,'Июнь'),
        (7,'Июль'),
        (8,'Август'),
        (9,'Сентябрь'),
        (10,'Октябрь'),
        (11,'Ноябрь'),
        (12,'Декабрь'),
    )

    YEARS = (
        (2019,'2019'),
        (2020,'2020'),
        (2021,'2021'),
        (2022,'2022'),
        (2023,'2023'),
        (2024,'2024'),
    )

    project = models.ForeignKey(Project, on_delete=models.SET('проект удален'))
    month = models.IntegerField(blank=True, choices=MONTHS)
    year = models.IntegerField(blank=True, choices=YEARS)
    file = models.FileField(upload_to='reports/%Y/%m/', blank=True)
    approval = models.IntegerField(blank=True, choices=ANSWER)
    expired = models.IntegerField(blank=True, choices=ANSWER)
    correct = models.IntegerField(blank=True, choices=ANSWER)
    sending_date = models.DateField(blank=True)
    approval_date = models.DateField(blank=True)
    date_change_status = models.DateField(blank=True)
    comment = models.CharField(max_length=255, blank=True)




