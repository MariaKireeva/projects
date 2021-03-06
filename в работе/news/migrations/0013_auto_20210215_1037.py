# Generated by Django 3.1.5 on 2021-02-15 07:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0012_auto_20210210_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(through='news.CategorySubscribers', to=settings.AUTH_USER_MODEL, verbose_name='Subscribers'),
        ),
    ]
