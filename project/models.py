from django.db import models

# Create your models here.



class Member(models.Model):

    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255, blank=True)
    fio_full = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    tell = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, blank=True)


class Project(models.Model):

    PORTFOLIOS = (
        ('DEMO', 'Демография'),
        ('ZDRV', 'Здравоохранение'),
        ('OBR', 'Образование'),
        ('ZGS', 'Жилье и городская среда'),
        ('BKAD', 'Безопасные и качественные автомобильные дороги'),
        ('CIF', 'Цифровая экономика'),
        ('MEZD', 'Международная кооперация и экспорт'),
        ('TRUD', 'Производительность труда и поддержка занятости'),
        ('MSP', 'Малое и среднее предпринимательство'),
        ('ECO', 'Экология'),
        ('CULT', 'Культура'),
    )

    NUM = (
        ('0', 'Нет'),
        ('1', 'Да'),
        ('2', 'Необходимо уточнение'),

    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    portfolio = models.CharField(max_length=4, choices=PORTFOLIOS, null=True, blank=True)
    code = models.CharField(max_length=3, null=True, blank=True)
    id_director = models.ManyToManyField(Member)
    id_administrator = models.ManyToManyField(Member)
    id_curator = models.ManyToManyField(Member)
    id_mentor = models.ManyToManyField(Member)
    id_support = models.ManyToManyField(Member)
    id_worker = models.ManyToManyField(Member)
    date_pasport = models.DateField()
    need_update = models.CharField(max_length=1, choices=NUM, blank=True)
    comment = models.CharField(max_length=255, blank=True)


