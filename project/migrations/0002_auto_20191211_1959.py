# Generated by Django 2.2.7 on 2019-12-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='need_update',
            field=models.CharField(choices=[('0', 'Нет'), ('1', 'Да'), ('2', 'Необходимо уточнение')], max_length=1),
        ),
    ]