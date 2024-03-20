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
    fathers_name = models.CharField(max_length=255, blank=True)
    telegram_id = models.IntegerField()
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

    def __str__(self) -> str:
        return self.name
    

class Audio(models.Model):
    name = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.name
