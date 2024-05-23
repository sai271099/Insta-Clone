# Generated by Django 2.2.2 on 2019-06-24 05:27

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190622_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfeed',
            name='slug',
            field=models.SlugField(default=posts.models.generate_id, max_length=25, unique=True),
        ),
    ]