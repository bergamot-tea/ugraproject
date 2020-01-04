# Generated by Django 2.2.7 on 2020-01-04 20:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0007_report_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('text', models.TextField(blank=True)),
                ('image1', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('image4', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('image5', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('date_open', models.DateField(auto_now_add=True)),
                ('date_change', models.DateField(auto_now=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Открыта'), (2, 'В работе'), (3, 'Закрыта')], default=1)),
                ('author', models.ForeignKey(on_delete=models.SET('пользователь удален'), to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=models.SET('проект удален'), to='project.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_post', models.DateField(auto_now_add=True)),
                ('text', models.TextField(blank=True)),
                ('image1', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, upload_to='screens/%Y/%m/%d')),
                ('author', models.ForeignKey(on_delete=models.SET('пользователь удален'), to=settings.AUTH_USER_MODEL)),
                ('id_issue', models.ForeignKey(on_delete=models.SET('заявка удалена'), to='issue.Issue')),
            ],
        ),
    ]
