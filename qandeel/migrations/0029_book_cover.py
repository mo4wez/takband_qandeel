# Generated by Django 4.2.7 on 2023-11-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qandeel', '0028_poet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='book/book_cover/', verbose_name='Book Cover'),
        ),
    ]