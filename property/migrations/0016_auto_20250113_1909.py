# Generated by Django 2.2.24 on 2025-01-13 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20250110_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
