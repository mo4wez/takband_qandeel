# Generated by Django 4.2.6 on 2023-11-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0005_alter_section_poetic_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='poet',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]