from typing import Iterable
from django.db import models


class Rates(models.Model):
    rate_name = models.CharField(max_length=300)
    rate_count = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.rate_name


class Place(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    telegram_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    house_number = models.CharField(max_length=30)
    apartment_number = models.CharField(max_length=30)
    entrance_number = models.CharField(max_length=30)
    floor_number = models.CharField(max_length=30)
    comment_to_address = models.TextField()
    rate = models.ForeignKey(Rates, on_delete=models.CASCADE, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    rate_count = models.CharField(max_length=300, blank=True, null=True)

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
    telegram_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_confirm = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.first_name


class ClientOrder(models.Model):
    client_id = models.ForeignKey(Account, to_field='telegram_id', on_delete=models.CASCADE)
    worker_id = models.ForeignKey(WorkerAccount, to_field='telegram_id', on_delete=models.CASCADE, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    photo = models.CharField(max_length=300, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.longitude or not self.latitude:
            if self.client_id:
                self.latitude = self.client_id.latitude
                self.longitude = self.client_id.longitude
                self.place = self.client_id.place
        return super().save(*args, **kwargs)
