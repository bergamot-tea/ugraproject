# Generated by Django 2.2.7 on 2020-02-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20200207_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='auditor',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]