# Generated by Django 2.2.7 on 2019-12-27 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20191227_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='comment',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
