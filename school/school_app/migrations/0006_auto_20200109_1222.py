# Generated by Django 2.0.2 on 2020-01-09 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0005_auto_20200109_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculties',
            name='url_Facebook',
        ),
        migrations.RemoveField(
            model_name='faculties',
            name='url_Instagram',
        ),
        migrations.RemoveField(
            model_name='faculties',
            name='url_Twitter',
        ),
    ]
