# Generated by Django 4.2.3 on 2023-07-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_city_country'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='city',
            constraint=models.UniqueConstraint(fields=('name', 'founding_date', 'demonym', 'ruler', 'area', 'population'), name='unique_city'),
        ),
    ]
