# Generated by Django 4.2.7 on 2023-11-05 01:33

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0017_alter_poet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_unicode=True, blank=True, editable=False, populate_from=['name'], unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_unicode=True, blank=True, editable=False, populate_from=['name'], unique=True),
        ),
    ]