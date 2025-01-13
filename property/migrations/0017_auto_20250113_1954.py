# Generated by Django 2.2.24 on 2025-01-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20250113_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='flats',
        ),
        migrations.AddField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(null=True, related_name='flats', to='property.Flat', verbose_name='Квартира, кототорая продается'),
        ),
    ]
