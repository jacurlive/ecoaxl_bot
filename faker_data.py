import django
import os
import random
from faker import Faker


def generate_fake_data(num: int) -> None:
    from account.models import UserLanguage

    fake = Faker()

    number = 12345678

    for _ in range(num):
        user_language = UserLanguage.objects.create(user_id=number, lang=fake.language_code())
        user_language.save()

        number += 1
        print(f"Created: {user_language}")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")

    django.setup()

    generate_fake_data(200)
