# Generated by Django 4.2.7 on 2023-11-05 01:26

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0016_alter_section_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poet',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_unicode=True, blank=True, editable=False, populate_from=['name'], unique=True),
        ),
    ]
