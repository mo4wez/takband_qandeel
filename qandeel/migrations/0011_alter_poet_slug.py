# Generated by Django 4.2.7 on 2023-11-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0010_alter_poet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]