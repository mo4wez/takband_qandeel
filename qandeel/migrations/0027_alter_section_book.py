# Generated by Django 4.2.7 on 2023-11-07 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0026_alter_poet_century'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='qandeel.book'),
        ),
    ]
