from typing import Iterable
from django.db import models


class Rates(models.Model):
    rate_name = models.CharField(max_length=300)
    rate_count = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()

    class Meta:
        verbose_name = ("Тариф")
        verbose_name_plural = ("Тарифы")


    def __str__(self) -> str:
        return self.rate_name


class Place(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = ("Район")
        verbose_name_plural = ("Районы")


    def __str__(self) -> str:
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.BigIntegerField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False, blank=True, null=True)
    is_confirm = models.BooleanField(default=False, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    house_number = models.CharField(max_length=30, blank=True, null=True)
    apartment_number = models.CharField(max_length=30, blank=True, null=True)
    entrance_number = models.CharField(max_length=30, blank=True, null=True)
    floor_number = models.CharField(max_length=30, blank=True, null=True)
    comment_to_address = models.TextField(blank=True, null=True)
    rate = models.ForeignKey(Rates, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    rate_count = models.CharField(max_length=300, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ("Клиенты")


    def save(self, *args, **kwargs):
        if not self.rate_count:
            self.rate_count = self.rate.rate_count
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class WorkerAccount(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField(unique=True)
    phone_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Курьер")
        verbose_name_plural = ("Курьеры")

    def __str__(self) -> str:
        return self.first_name


class ClientOrder(models.Model):
    client_id = models.ForeignKey(Account, to_field='telegram_id', on_delete=models.CASCADE)
    worker_id = models.ForeignKey(WorkerAccount, to_field='telegram_id', on_delete=models.CASCADE, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_taken = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    house_number = models.CharField(max_length=30, blank=True, null=True)
    apartment_number = models.CharField(max_length=30, blank=True, null=True)
    entrance_number = models.CharField(max_length=30, blank=True, null=True)
    floor_number = models.CharField(max_length=30, blank=True, null=True)
    comment_to_address = models.TextField(blank=True, null=True)
    comment_to_order = models.TextField(blank=True, null=True)
    client_photo = models.CharField(max_length=300, blank=True, null=True)
    worker_photo = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = ("Заказы")
        verbose_name_plural = ("Заказы")


    def save(self, *args, **kwargs):
        if not self.longitude or not self.latitude:
            if self.client_id:
                self.latitude = self.client_id.latitude
                self.longitude = self.client_id.longitude
                self.place = self.client_id.place
                self.house_number = self.client_id.house_number
                self.apartment_number = self.client_id.apartment_number
                self.entrance_number = self.client_id.entrance_number
                self.floor_number = self.client_id.floor_number
                self.comment_to_address = self.client_id.comment_to_address

        return super().save(*args, **kwargs)


class UserLanguage(models.Model):
    user_id = models.BigIntegerField(unique=True)
    lang = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Язык клиента")
        verbose_name_plural = ("Язык клиентов")
