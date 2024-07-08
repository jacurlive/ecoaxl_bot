import django
import os
from faker import Faker


def generate_fake_data(num: int) -> None:
    from account.models import UserLanguage, Account, Rates, Place, WorkerAccount

    fake = Faker()

    rate_instance = Rates.objects.get(pk=1)
    place_instance = Place.objects.get(pk=1)

    number = 12345673

    for _ in range(num):
        # user_language = UserLanguage.objects.create(user_id=number, lang=fake.language_code())
        # user_language.save()
        # account = Account.objects.create(
        #     name=fake.name(),
        #     telegram_id=number, 
        #     phone_number=fake.phone_number(),
        #     is_active=True,
        #     is_confirm=True,
        #     latitude=fake.latitude(),
        #     longitude=fake.longitude(),
        #     house_number=12,
        #     apartment_number=12,
        #     entrance_number=12,
        #     floor_number=12,
        #     place=place_instance,
        #     rate=rate_instance
        #     )
        worker = WorkerAccount.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            telegram_id=number,
            phone_number=fake.phone_number(),
            is_active=True,
            is_confirm=True
        )
        number += 1
        print(f"Created: {worker}")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")

    django.setup()

    generate_fake_data(500)
