# Generated by Django 3.0.7 on 2020-11-08 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
