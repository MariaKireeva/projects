# Generated by Django 3.1.5 on 2021-02-10 08:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0011_auto_20210210_1005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='topic',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='post_category',
        ),
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(through='news.CategorySubscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
    ]