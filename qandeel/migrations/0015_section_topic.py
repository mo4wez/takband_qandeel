# Generated by Django 4.2.7 on 2023-11-04 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0014_alter_section_poetic_format_alter_topic_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='qandeel.topic'),
        ),
    ]
