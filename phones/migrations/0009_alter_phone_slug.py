# Generated by Django 4.1 on 2022-08-31 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0008_remove_phone_url_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
