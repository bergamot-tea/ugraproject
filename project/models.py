from django.db import models

# Create your models here.

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
    portfolio = models.CharField(max_length=4, choices=PORTFOLIOS)
    code = models.CharField(max_length=3)
    id_director = models.IntegerField()
    id_administrator = models.IntegerField()
    id_curator = models.IntegerField()
    id_mentor = models.IntegerField()
    id_support = models.IntegerField()
    id_worker = models.IntegerField()
    date_pasport = models.DateField()
    need_update = models.CharField(max_length=1, choices=NUM)
    comment = models.CharField(max_length=255)

