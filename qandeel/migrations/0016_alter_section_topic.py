# Generated by Django 4.2.7 on 2023-11-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0015_section_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='qandeel.topic'),
        ),
    ]