# Generated by Django 3.0.3 on 2020-02-26 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0002_auto_20200226_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='slug',
            field=models.SlugField(default='racdyAZd'),
        ),
    ]
