# Generated by Django 2.0.2 on 2020-01-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0006_auto_20200109_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculties',
            name='url_Facebook',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='faculties',
            name='url_Instagram',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='faculties',
            name='url_Twitter',
            field=models.URLField(default=''),
        ),
    ]