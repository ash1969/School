# Generated by Django 2.0.2 on 2020-01-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_pictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='description',
            field=models.CharField(default='MLRP Public School Event', max_length=1000),
            preserve_default=False,
        ),
    ]
