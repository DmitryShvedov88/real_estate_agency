# Generated by Django 2.2.24 on 2024-11-21 18:21
import phonenumbers
from django.db import migrations


def normalize_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        normal_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if not phonenumbers.is_valid_number(normal_number):
            normal_number = None
        flat.owner_pure_phone = normal_number
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(
            normalize_numbers,
            move_backward
            ),
    ]