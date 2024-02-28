from django.contrib import admin
from .models import Account, Rates, Address, Place


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "fathers_name", "phone_number", "is_active", "is_confirm", "rate", "place")


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display = ("id", "rate_name", "rate_count", "price")
    list_display_links = ("id", "rate_name")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "latitude", "longitude")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
