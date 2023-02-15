from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    new_building = models.BooleanField(
        'Новостройка',
        null=True,
        db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    likes = models.ManyToManyField(
        User,
        blank=True,
        related_name='liked_flats',
        verbose_name='Кому понравилось'
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complain(models.Model):
    author = models.ForeignKey(
        User,
        related_name='user_complains',
        verbose_name='Кто жалуется',
        on_delete=models.CASCADE
    )
    flat = models.ForeignKey(
        Flat,
        related_name='flat_complains',
        verbose_name='Квартира в жалобе',
        on_delete=models.CASCADE
    )
    text = models.TextField("Текст жалобы")

    def __str__(self):
        return f"{self.author}: {self.complain_text}"


class Owner(models.Model):
    owner_name = models.CharField("ФИО владельца", db_index=True, max_length=200)
    owners_phonenumber = models.CharField(
        "Номер владельца", db_index=True, max_length=20)
    owner_pure_phone = PhoneNumberField(
        'Нормализованный номер владельца',
        db_index=True, blank=True, null=True)
    owners_flats = models.ManyToManyField(
        Flat, related_name='owned_apartments_info',
        db_index=True, verbose_name='Квартиры в собственности', blank=True)

    def __str__(self):
        return f"{self.owner_name}, {self.owner_pure_phone}"