# Generated by Django 3.2.12 on 2022-07-05 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_article_article_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 7, 5, 14, 39, 15, 16967), max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 5, 14, 39, 15, 16016), verbose_name='date publiched'),
        ),
    ]