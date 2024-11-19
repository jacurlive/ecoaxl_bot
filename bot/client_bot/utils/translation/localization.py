# Модуль для работы с переводами
class Localization:
    translations = {
        'none': {
            "welcome": "Assalomu alaykum! Xush kelibsiz. Iltimos, tilni tanlang. 🇺🇿\n\nЗдравствуйте! Добро пожаловать. Пожалуйста, выберите язык. 🇷🇺",
            "error": "Nimadir notog'ri ketdi. 🇺🇿\n\nЧто-то пошло не так. 🇷🇺"
        },
        'uz': {
            "greeting_registered": """
🌟 Botdan foydalanishni boshlash uchun quyidagi buyruqlardan foydalaning:

➡️ /start - Ishlatishni boshlash yoki qayta boshlash uchun

📋 Profilingiz haqida to‘liq ma’lumot olish uchun Profil tugmasini bosing.
📞 Administrator bilan bog‘lanish uchun Yordam tugmasini bosing.
            """,
            "greeting_not_registered": """
🌿 Hurmatli foydalanuvchi, assalomu alaykum!

Biz sizga ECO AXL xizmatini taklif etamiz, u sizga uy chiqindilaridan chiqmasdan qutulishga yordam beradi! 🚮

🏠 Biz kvartiralar va xususiy uylar uchun maishiy chiqindilarni olib chiqamiz.

Har qanday obunada 7 kg gacha bo‘lgan 5 ta sumkadan ortiq bo‘lmagan chiqindi olib chiqish imkoniyati mavjud.

Bizning xizmatimiz quyidagi toifadagi odamlar uchun mos:

🧑‍💻🧑‍🔧 Ishbilarmon va band odamlar uchun.

🎮 Geymerlar va uyda o‘tiradiganlar uchun foydali.

👩‍👧‍👦 Dekretdagi onalarga yordam beramiz.

🧑‍🦳👨‍🦳 Keksalarga obuna rasmiylashtiring.

😷 Kasallik tufayli ko‘chaga chiqmaydiganlar uchun.

👨‍🦽 Harakatlanishi cheklangan fuqarolar uchun zarur.

            """,
            "confirmation": """
❗️Iltimos, foydalanuvchi shartnomasi bilan tanishing❗️

Va quyida tanlang
            """,
            "get_name": """
📝 Ro‘yxatdan o‘tish jarayonini boshlaylik. Familiya, ism, otangizning ismini quyidagi formatda kiriting: 

✍️ Familiya Ism Otasining ismi. 

(Bo‘sh joy qoldiring!)

""",
            "get_contact": "📱 Quyidagi tugma orqali kontaktni yuboring.",
            "error_name_format": """
❌ Format noto‘g‘ri❗️

✍️ Familiya, ism, otangizning ismini quyidagi formatda kiriting: Familiya Ism Otasining ismi. 

(Bo‘sh joy qoldiring!)

""",
            "get_location": """
📍 Manzilingizni yuboring.

📝 Muhim eslatma: Uy manzilingizni yuboring, chunki bu aniq manzilni aniqlash uchun muhim.

            """,
            "get_address": """
🏠 Manzilingizni quyidagi formatda kiriting:

Uy/kvartira/Podyezd/Qavat

Misol: 30/16/2/1

            """,
            "get_comment_to_address": """
📝 Manzil bo‘yicha sharhlar:

Sizni tezroq va aniqroq topishimizga yordam berish uchun qoʻshimcha maʼlumotlarni kiriting. Masalan, diqqatga sazovor joylar, binoga kirish uchun maxsus ko'rsatmalar yoki kurer uchun foydali bo'lishi mumkin bo'lgan boshqa eslatmalar.
""",
            "error_address_format": """
❌ Format noto‘g‘ri❗️

🏠 Manzilingizni quyidagi formatda kiriting:

Uy/kvartira/Podyezd/Qavat

Misol: 30/16/2/1

            """,
            "complete_registration": "🎉 Ro‘yxatdan o‘tganingiz uchun rahmat!",
            "error": "⚠️ Nimadir noto‘g‘ri ketdi❗️",
            "register_btn": "Ro'yhatdan o'tish",
            "help_btn": "Yordam",
            "get_location_btn": "Joylashuvni yuborish",
            "get_place": "🗺 Tumanni tanlang:",
            "get_rate": """
📆 “Start” tarifi bo‘yicha maishiy chiqindilarni juft va toq kunlarda olib chiqish xizmati mavjud.

Tariff nomi: "Start".

💳 To'lov Click yoki Payme orqali amalga oshiriladi.

💸 Xizmat narxi: 100,000 so‘m (har oyda 15 marta chiqindi olib chiqish kiradi).

-------------------------------------------------

📆 "VIP" tarifi bo‘yicha maishiy chiqindilarni juft va toq kunlarda olib chiqish xizmati mavjud.

Tariff nomi: "VIP".

💳 To'lov Click yoki Payme orqali amalga oshiriladi.

💸 Xizmat narxi: 200,000 so‘m (har oyda 30 marta chiqindi olib chiqish kiradi).



🛎 To‘lovni tasdiqlash uchun sizga ilovada to‘lov haqida bildirishnoma keladi.

            """,
            "already_registered": "✅ Siz allaqachon ro‘yxatdan o‘tgansiz!",
            "profile_error": "🚫 Siz hali ro‘yxatdan o‘tmagansiz.",
            "profile_btn": "Profil",
            "create_order_btn": "Buyurtma yaratish",
            "actual_order_btn": "Joriy buyurtma",
            "name_btn": "Ism",
            "house_number_btn": "Uy raqami",
            "apartment_number_btn": "Kvartira raqami",
            "entrance_number_btn": "Kirish raqami",
            "floor_number_btn": "Qavat",
            "comment_btn": "Manzilga sharhlar",
            "change_profile": "🛠 O‘zgartirmoqchi bo‘lgan maydonni tanlang:",
            "change_name_message": "✍️ Yangi ismingizni kiriting:",
            "change_house_message": "🏠 Uy raqamini kiriting:",
            "change_apartment_message": "🏢 Kvartira raqamini kiriting:",
            "change_entrance_message": "🚪 Podyezd raqamini kiriting:",
            "change_floor_message": "🏙 Qavat raqamini kiriting:",
            "change_comment_message": "✍️ Manzil bo‘yicha sharhlarni kiriting:",
            "error_changing": "Tugmani bosing",
            "complete_changing": "✅ Ma'lumotlar muvaffaqiyatli o‘zgartirildi!",
            "confirm_btn": "Tasdiqlash✅",
            "cancel_btn": "Rad etish❌",
            "delete_btn": "Akkaunt o'chirish❌",
            "edit_btn": "Profilni tahrirlash",
            "back_btn": "◀️Orqaga",
            "help_message": "💬 Operator bilan bog‘lanish uchun havola: @ECOAXL | @ECOAXL2",
            "rate_count_error": "🛑 Buyurtmalaringiz tugadi, qolgan buyurtmalar soni - 0",
            "order_success": "📝 Buyurtma yaratildi - qolgan buyurtmalaringiz soni:",
            "photo_load_error": "⚠️ Rasmni yuklashda xatolik yuz berdi!",
            "name": "Ism:",
            "phone_number": "Kontakt:",
            "house_number": "Uy:",
            "apartment_number": "Kvartira",
            "entrance_number": "Kirish:",
            "floor": "Qavat:",
            "comment_to_address": "Izoh:",
            "active": "Faol🟢",
            "not_active": "Faol emas🔴",
            "status": "Holat:",
            "deleted_success": "✅ Hisob muvaffaqiyatli o‘chirildi!",
            "accept_photo": "📸 Eshingizning oldidagi paketlarning fotosuratini yuboring, shunda kuryer aynan sizning buyurtmangizni olib ketishi mumkin.",
            "not_ended_order_error": """
⏳ Sizda tugallanmagan buyurtma mavjud, kuryerimiz yaqin orada buyurtmangizni yakunlaydi.

Agar muammo bo'lsa, Yordam tugmasini bosing.
""",
            "not_order_error": "📦 Sizda hali mavjud buyurtmalar yo'q, Buyurtma yaratish tugmasini bosing.",
            "worker_status": "Kuryer holati:",
            "order_created_time": "Yaratilish vaqti:",
            "order_end": "Tugallandi🟢",
            "order_not_end": "Tugallanmagan🔴",
            "order_status": "Holat:",
            "default_message": "To'liq ma'lumot olish uchun buyruqni kiriting / help",
            "get_contact_btn": "Raqamni yuborish",
            "change_language_btn": "Tilni o'zgartirish",
            "change_language": "🌐 Tilni tanlang:",
            "change_language_success": "✅ Til muvaffaqiyatli o'zgartirildi!",
            "back_message": """
Botdan foydalanish uchun quidagi tugmalardan foydalaning:

Profil - profilingiz xaqida malumot
Yordam - administrator bilan bog'lanish
            """,
            "active_customer": "🎉 Profilingiz muvaffaqiyatli faollashtirildi! Endi botdan foydalanishingiz mumkin!",
            "activation_error": "⚠️ Xatolik yuz berdi, iltimos, keyinroq urinib ko'ring yoki administrator bilan bog'laning.",
            "not_registered_customer": "Siz ro'yhatga olinmagansiz iltimos administrator bilan bog'laning",
            "additions_message": "Qo'shimcha ma'lumot qo'shish uchun quyida tanlang.",
            "success_photo": "Rasim joylandi",
            "order_count": "Chiqarishlar soni:",
            "account_activation": "Akkauntni faolashtirish",
            "register_type": "Ro'yhatdan o'tish usulini tanlang",
            "buy_rate": "Tariflar",
            "payment_type": "To'lov turini tanlang",
            "yes": "Xa",
            "no": "Yoq",
            "create_order": "Buyurtma yaratmoqchimisiz",
            "buy_rate_success": "Buyurtma xarid qilish jarayoni muvafaqiyatli otdi.\nBuyurtmalar qoldig'i: ",
            "cancel_confirmation": "Botni qayta yuritish uchun /start buyrugini yuboring"},

        'ru': {
            "greeting_registered": """
Добро пожаловать!

Для начала использования бота или его перезапуска используйте команду:

/start

Навигация по боту:

📋 Профиль - Полная информация о вашем аккаунте.

❓ Помощь - Связаться с администратором.

Приятного использования! 😊
                    """,
            "greeting_not_registered": """
Добрый день, дорогой пользователь! 🌟

Мы рады представить вам сервис ECO AXL, который поможет вам избавиться от бытового мусора, не выходя из дома!

🗑️ Что мы предлагаем:

    Вынос бытового мусора из квартир и частных домов.
    По любой подписке доступен вынос до 5 мешков весом до 7 кг.

📦 Наш сервис подходит для:

    Деловых и занятых людей 🧑‍💻🧑‍🔧
    Геймеров и домоседов 🎮
    Мам в декрете 👩‍👧‍👦
    Пожилых людей 🧑‍🦳👨‍🦳 (оформите подписку для своих близких)
    Тех, кто болеет и не выходит на улицу 😷
    Маломобильных граждан 👨‍🦽

Мы здесь, чтобы облегчить вашу жизнь. 🌿
                    """,
            "confirmation": """
❗️Прочитайте пожалуйста пользовательское соглашение❗️

И Выберите ниже
""",
            "get_name": """
Давайте начнем процесс регистрации. 📝

Пожалуйста, введите ваше Ф.И.О. в формате:

Фамилия Имя Отчество

⚠️ Важно: Введите данные через пробел!
""",
            "get_contact": "📲 Пожалуйста, отправьте ваш контакт, используя кнопку ниже.",
            "error_name_format": """
❗️ У вас неправильный формат! ❗️

Пожалуйста, введите ваше Ф.И.О в формате:

Фамилия Имя Отчество

Через пробел!
""",
            "get_location": """
📍 Отправьте локацию

⚠️ Важное примечание: Пожалуйста, отправляйте ваш домашний адрес, так как это важно для определения точного местоположения.
                           """,
            "get_address": """
🏡 Введите ваш адрес в формате:

Дом/Квартира/Подъезд/Этаж

Пример: 30/16/2/1
""",
            "get_comment_to_address": """
📝 Комментарии к адресу:

Пожалуйста, укажите дополнительные детали, которые помогут нам найти вас быстрее и точнее. Например, ориентиры, особые инструкции по входу в здание или любые другие примечания, которые могут быть полезны курьеру.
""",
            "error_address_format": """
❗️ У вас неправильный формат!

Введите ваш адрес в формате:

Дом/Квартира/Подъезд/Этаж

📍 Пример: 30/16/2/1
    """,
            "complete_registration": """
🎉 Спасибо за регистрацию!

Мы рады приветствовать вас в сервисе ECO AXL!

Теперь вы можете воспользоваться нашим сервисом по вывозу бытового мусора. Если у вас возникнут вопросы или потребуется помощь, не стесняйтесь обращаться к нам.
""",
            "error": """
⚠️ Что-то пошло не так!

К сожалению, возникла ошибка во время обработки вашего запроса. Пожалуйста, попробуйте еще раз или свяжитесь с нашей службой поддержки для получения помощи.
""",
            "register_btn": "Пройти Регистрацию",
            "help_btn": "Помощь",
            "get_location_btn": "Отправить локацию",
            "get_place": """
🏙️ Выберите район:

Пожалуйста, укажите свой район для более точного обслуживания. Выбор района поможет нам лучше понять ваши потребности и предложить наиболее подходящие услуги.

Нажмите на кнопку ниже, чтобы сделать свой выбор!
""",
            "get_rate": """
💰 Доступный тариф: "Start"

Доступен тариф "Start" для выноса бытового мусора, который действует как по четным, так и по нечетным числам.

🛠️ Что включает тариф:

    Стоимость услуги: 100,000 сум
    В тариф входит 15 выбросов в месяц!

💳 Форматы оплаты:

    Click
    Payme

----------------------------------------
    
💰 Доступный тариф: "VIP"

Доступен тариф "VIP" для выноса бытового мусора, который действует как по четным, так и по нечетным числам.

🛠️ Что включает тариф:

    Стоимость услуги: 200,000 сум
    В тариф входит 30 выбросов в месяц!

💳 Форматы оплаты:

    Click
    Payme
""",
            "already_registered": """
🚫 Вы уже зарегистрированы!

Похоже, что ваша регистрация уже была выполнена.

💬 Помощь:

Если у вас возникли вопросы или вам нужна поддержка, нажмите на кнопку Помощь.

🔧 Профиль:

Чтобы изменить информацию о вашем аккаунте, используйте кнопку Профиль.
""",
            "profile_error": """
🚫 Вы еще не зарегистрировались!

Пожалуйста, пройдите процесс регистрации, чтобы получить доступ к всем функциям нашего сервиса.
""",
            "profile_btn": "Профиль",
            "create_order_btn": "Создать заказ",
            "actual_order_btn": "Актуальный заказ",
            "name_btn": "Имя",
            "house_number_btn": "номер дома",
            "apartment_number_btn": "номер квартиры",
            "entrance_number_btn": "номер подьезда",
            "floor_number_btn": "этаж",
            "comment_btn": "комментарии к адресу",
            "change_profile": "🛠️ Выберите поле, которое хотите изменить:",
            "change_name_message": "✏️ Введите ваше новое имя:",
            "change_house_message": "🏠 Введите номер вашего дома:",
            "change_apartment_message": "🏢 Введите номер вашей квартиры:",
            "change_entrance_message": "🚪 Введите номер подъезда:",
            "change_floor_message": "🏢 Введите номер этажа:",
            "change_comment_message": """
📝 Введите комментарии к адресу:

Здесь вы можете оставить дополнительные сведения или указания, которые могут быть полезны для курьера.
""",
            "error_changing": "Нажмите на кнопку",
            "complete_changing": """
✅ Данные успешно изменены!

Ваши изменения были сохранены. Если вам нужно внести дополнительные правки, нажмите на кнопку Профиль
""",
            "confirm_btn": "Потвердить✅",
            "cancel_btn": "Отказать❌",
            "delete_btn": "Удалить аккаунт❌",
            "edit_btn": "Редакторовать профиль",
            "back_btn": "◀️Назад",
            "help_message": """
💬 Связаться с оператором:

Для получения дополнительной информации или помощи, пожалуйста, свяжитесь с нашим оператором: @ECOAXL | @ECOAXL2
""",
            "rate_count_error": """
❗️ Внимание:
У вас исчерпаны все заказы. Осталось 0 заказов.
""",
            "order_success": """
✅ Заказ успешно создан!
Ваш текущий остаток заказов:
""",
            "photo_load_error": """
❌ Ошибка!

Не удалось загрузить фотографию.
""",
            "name": "имя:",
            "phone_number": "номер телефона:",
            "house_number": "номер дома:",
            "apartment_number": "номер квартиры:",
            "entrance_number": "номер подьезда:",
            "floor": "этаж:",
            "comment_to_address": "комментарии к адресу:",
            "active": "Активен🟢",
            "not_active": "Неактивен🔴",
            "status": "Статус:",
            "deleted_success": """
✅ Успех!
Ваш аккаунт был успешно удалён.
""",
            "accept_photo": """
📸 Отправьте фотографию пакетов, расположенных возле вашей двери.
Это поможет курьеру точно идентифицировать ваш заказ.
""",
            "not_ended_order_error": """
⚠️ У вас есть незавершённый заказ!
В ближайшее время наш курьер завершит его. Если у вас возникли вопросы или проблемы, нажмите на кнопку Помощь.
""",
            "not_order_error": """
📭 У вас ещё нет актуальных заказов.
Пожалуйста, нажмите на кнопку Создать заказ, чтобы оформить новый!
""",
            "worker_status": "Статус курьера:",
            "order_created_time": "Время создания:",
            "order_end": "Закончен🟢",
            "order_not_end": "Незакончен🔴",
            "order_status": "Статус:",
            "default_message": "Если у вас возникли вопросы или вам нужна поддержка, нажмите на кнопку Помощь.",
            "get_contact_btn": "Отправить контакт",
            "change_language_btn": "Изменить язык",
            "change_language": """
🌐 Выберите язык:
Пожалуйста, выберите язык, на котором вы хотите продолжить использование сервиса.
""",
            "change_language_success": """
🎉 Язык успешно изменён! ✅
Теперь вы можете продолжать использовать сервис на выбранном языке.
""",
            "back_message": """
Для начала использования бота или его перезапуска используйте команду:

/start

Навигация по боту:

📋 Профиль - Полная информация о вашем аккаунте.

❓ Помощь - Связаться с администратором.

Приятного использования! 😊
            """,
            "active_customer": """
🎉 Ваш профиль успешно активирован!
Теперь вы можете пользоваться ботом без ограничений. Приятного использования!
""",
            "activation_error": """
❗️ Произошла ошибка!
Пожалуйста, попробуйте снова позже. Если проблема не исчезнет, свяжитесь с администратором.
""",
            "not_registered_customer": """
❗️ Вы не зарегистрированы!
Пожалуйста, свяжитесь с администратором для регистрации.
""",
            "additions_message": "📋 Для добавления дополнительных сведений, пожалуйста, выберите ниже:",
            "success_photo": "🖼️ Фотография успешно добавлена!",
            "order_count": "Количество выносов:",
            "account_activation": "Активировать аккаунт",
            "register_type": """
📋 Выберите способ регистрации:

    1. Активировать аккаунт - если вы прошли регистрацию через оператора
    2. Пройти регистрацию - для активации аккаунта
""",
            "buy_rate": "Тарифы",
            "payment_type": "❗️Выберите способ оплаты",
            "yes": "Да",
            "no": "Нет",
            "create_order": "Вы точно хотите создать заказ",
            "buy_rate_success": "Покупка тарифа прошла успешно.\nВаш остаток заказов: ",
            "cancel_confirmation": "Для рестарта бота введите комманду /start"
        }
    }

    @staticmethod
    def get_translation(language, key):
        return Localization.translations.get(language, {}).get(key, key)


# Функция для отправки локализованных сообщений
async def get_localized_message(language, key):
    translation = Localization.get_translation(language, key)
    return translation
