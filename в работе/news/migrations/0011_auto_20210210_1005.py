# Generated by Django 3.1.5 on 2021-02-10 07:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0010_auto_20210210_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(through='news.CategorySubscribers', to=settings.AUTH_USER_MODEL),
        ),
    ]
