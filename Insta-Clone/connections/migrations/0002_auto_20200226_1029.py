# Generated by Django 3.0.3 on 2020-02-26 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='slug',
            field=models.SlugField(default='QjaV4loN'),
        ),
    ]
