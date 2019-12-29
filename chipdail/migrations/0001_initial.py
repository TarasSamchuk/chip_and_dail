# Generated by Django 2.2.7 on 2019-11-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('place', models.TextField(blank=True, db_index=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('start_work', models.DateTimeField(blank=True, null=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]