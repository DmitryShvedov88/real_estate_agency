from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    '''Class Flat'''
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now, db_index=True
        )
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50, db_index=True
        )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50, blank=True, help_text='Чертаново Южное'
        )
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж'
        )
    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True
        )
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True, blank=True, db_index=True
        )
    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField(
        'Активно-ли объявление',
        db_index=True
        )
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True, blank=True,
        )
    new_building = models.BooleanField(
        'Новостройка',
        null=True, blank=True
        )
    likes = models.ManyToManyField(
        User,
        verbose_name='Лайк',
        blank=True, related_name="flats"
        )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaints(models.Model):
    '''Complaints class'''
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь, который жалуется",
        on_delete=models.CASCADE,
        null=True, blank=True, related_name="сomplaints"
        )
    flat = models.ForeignKey(
        Flat, verbose_name="Квартира, на которую жалуются", on_delete=models.CASCADE,
        null=True, blank=True, related_name="complaints"
        )
    description = models.TextField(
        null=True, blank=True, verbose_name="Текст жалобы"
        )

    def __str__(self):
        return f"{self.user} {self.flat}"


class Owner(models.Model):
    '''Owner class'''
    name = models.CharField(
        'ФИО владельца',
        max_length=200, null=True, help_text='ФИО владельца', db_index=True
        )
    phone = models.CharField(
        'Номер владельца',
        null=True, max_length=20
        )
    pure_phone = PhoneNumberField(
        "Нормализованный телефон владельца",
        blank=True, null=True, max_length=20
        )
    flat = models.ManyToManyField(
        Flat, verbose_name="Квартира, кототорая продается",
        null=True, related_name="flats"
        )

    def __str__(self):
        return f"{self.name} {self.pure_phone}"
