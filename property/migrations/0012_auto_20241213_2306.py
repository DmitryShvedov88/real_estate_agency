# Generated by Django 2.2.24 on 2024-12-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner_to_flat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, help_text='ФИО владельца', max_length=200, null=True, verbose_name='ФИО владельца'),
        ),
    ]
