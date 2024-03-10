from django.contrib import admin
from .models import Account, Rates, Place


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "telegram_id", "phone_number", "is_active", "is_confirm", "rate", "place")
    list_display_links = ("id", "name", "telegram_id", "phone_number")


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display = ("id", "rate_name", "rate_count", "price")
    list_display_links = ("id", "rate_name")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
