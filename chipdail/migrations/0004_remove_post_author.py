# Generated by Django 2.2.7 on 2019-12-04 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chipdail', '0003_auto_20191202_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
