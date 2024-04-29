from django.contrib import admin
from .models import Account, Rates, Place, WorkerAccount, ClientOrder


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


@admin.register(WorkerAccount)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "telegram_id", "phone_number", "is_active", "is_confirm")
    list_display_links = ("id", "first_name", "last_name", "telegram_id", "phone_number")


@admin.register(ClientOrder)
class ClientOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "client_id", "worker_id", "photo", "is_completed", "is_taken", "created_date")
    list_display_links = ("id", "client_id", "worker_id")
    list_editable = ("is_completed", "is_taken")
