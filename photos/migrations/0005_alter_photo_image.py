# Generated by Django 4.2.3 on 2023-07-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_city_unique_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/images/', verbose_name='Картинка'),
        ),
    ]