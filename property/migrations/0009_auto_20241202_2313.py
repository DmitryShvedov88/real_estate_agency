# Generated by Django 2.2.24 on 2024-12-02 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20241121_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flat', to='property.Flat', verbose_name='Квартира, на которую жалуются'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который жалуется'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Лайк'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный телефон владельца'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ФИО владельца', max_length=200, null=True, verbose_name='ФИО владельца')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None, verbose_name='Нормализованный телефон владельца')),
                ('flats', models.ManyToManyField(null=True, related_name='flats', to='property.Flat', verbose_name='Квартира, кототорая продается')),
            ],
        ),
    ]
