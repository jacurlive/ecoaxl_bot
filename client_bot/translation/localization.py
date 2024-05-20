# Модуль для работы с переводами
class Localization:
    translations = {
        'none': {
            "welcome": "Assalomu alaykum! Xush kelibsiz. Iltimos, tilni tanlang. 🇺🇿\n\nЗдравствуйте! Добро пожаловать. Пожалуйста, выберите язык. 🇷🇺",
            "error": "Nimadir notog'ri ketdi. 🇺🇿\n\nЧто-то пошло не так. 🇷🇺"
        },
        'uz': {
            "greeting_registered": "Assalomu alaykum!registered",
            "greeting_not_registered": "Assalomu alaykum!NOT registered",
            "confirmation": "confirmation uz",
            "get_name": "get full name uz",
            "get_contact": "get_contact uz",
            "error_name_format": "error_name_format uz",
            "get_location": "get_location uz",
            "get_address": "get_address uz",
            "get_comment_to_address": "get_comment_to_address uz",
            "error_address_format": "error_address_format uz",
            "complete_registration": "complete_registration uz",
            "error": "error uz",
            "register_btn": "Ro'yhatdan o'tish",
            "help_btn": "Yordam",
            "get_location_btn": "get_location_btn uz",
            "get_place": "get_place uz",
            "get_rate": "get_rate uz",
            "already_registered": "already_registered uz",
            "profile_error": "profile_error uz",
            "profile_btn": "profile_btn uz",
            "create_order_btn": "create_order_btn uz",
            "actual_order_btn": "actual_order_btn uz",
            "name_btn": "name_btn uz",
            "house_number_btn": "house_number_btn uz",
            "apartment_number_btn": "apartment_number_btn uz",
            "entrance_number_btn": "entrance_number_btn uz",
            "floor_number_btn": "floor_number_btn uz",
            "comment_btn": "comment_btn uz",
            "change_profile": "change_profile uz",
            "change_name_message": "change_name_message uz",
            "change_house_message": "change_house_message uz",
            "change_apartment_message": "change_apartment_message uz",
            "change_entrance_message": "change_entrance_message uz",
            "change_floor_message": "change_floor_message uz",
            "change_comment_message": "change_comment_message uz",
            "error_changing": "error_changing uz",
            "complete_changing": "complete_changing uz",
            "confirm_btn": "confirm_btn uz",
            "cancel_btn": "cancel_btn uz",
            "delete_btn": "delete_btn uz",
            "edit_btn": "edit_btn uz",
            "back_btn": "back_btn uz",
            "help_message": "help_message uz",
            "rate_count_error": "rate_count_error uz",
            "order_success": "order_success uz",
            "photo_load_error": "photo_load_error uz",
            "name": "name uz",
            "phone_number": "phone_number uz",
            "house_number": "house_number uz",
            "apartment_number": "apartment_number uz",
            "entrance_number": "entrance_number uz",
            "floor": "floor uz",
            "comment_to_address": "comment_to_address uz",
            "active": "active uz",
            "not_active": "not_active uz",
            "status": "status uz",
            "deleted_success": "deleted_success uz",
            "accept_photo": "accept_photo uz",
            "not_ended_order_error": "not_ended_order_error uz",
            "not_order_error": "not_order_error uz",
            "worker_status": "worker_status uz",
            "order_created_time": "order_created_time uz",
            "order_end": "order_end uz",
            "order_not_end": "order_not_end uz",
            "order_status": "order_status uz",
            "default_message": "default_message uz"
        },
        'ru': {
            "greeting_registered": """
Для пользования бота можете использовать следующие комманды:

/start - Для начала использования или для рестарта

Нажмите на кнопку - Профиль - для полной информации вашего аккаунта
Нажмите на кнопку - Помощь - что бы связаться с администратором
                    """,
            "greeting_not_registered": """
Добрый день дорогой пользователь! 

Мы предлагаем тебе сервис ECO AXL  который поможет вам избавиться от бытового мусора не выходя из дома!

Выносим бытовой мусор из квартир и частных домов.

По любой Подписке доступен вынос не более 5ти мешков весом до 7 кг


наш сервис подходит для людей следующих категорий: 

Для деловых и занятых людей.  🧑‍💻🧑‍🔧

Полезны для геймеров и домоседов.🎮

Помогаем мамам в декрете.👩‍👧‍👦

Оформите подписку пожилым людям🧑‍🦳👨‍🦳

Для тех кто болеет и не выходит на улицу😷

Необходимы маломобильным гражданам👨‍🦽
                    """,
            "confirmation": """
<b>Пользовательское соглашение для Telegram бота</b>

Пожалуйста, обратите внимание, что следующее пользовательское соглашение представляет собой общие правила и условия использования Telegram бота, занимающегося коммерцией в сфере услуг. Эти условия описывают взаимоотношения между владельцем бота и его пользователями. Пожалуйста, внимательно прочитайте их перед использованием бота.

<b>1. Предоставление услуг</b>
        1.1. Владелец бота предлагает услуги через Telegram бота и обязуется предоставлять их в соответствии с описанием услуг, предоставленным в боте.
        1.2. Владелец бота оставляет за собой право изменять, обновлять или прекращать предоставление любых услуг в любое время без предварительного уведомления пользователя.

<b>2. Ограничение ответственности</b>
        2.1. Владелец бота не несет ответственности за любые прямые или косвенные убытки, понесенные пользователями в результате использования услуг, предоставляемых ботом.
        2.2. Владелец бота не несет ответственности за проблемы, возникающие из-за неправильного использования бота или неправильной интерпретации предоставленной информации.
        2.3. Владелец бота не несет ответственности за любые проблемы, связанные с Telegram платформой или взаимодействием с другими ботами или сторонними сервисами.

<b>3. Конфиденциальность</b>
        3.1. Владелец бота обязуется обрабатывать персональные данные пользователей в соответствии с применимым законодательством о защите данных.
        3.2. Владелец бота не будет передавать персональные данные пользователей третьим лицам без их предварительного согласия, за исключением случаев, предусмотренных законодательством.

<b>4. Интеллектуальная собственность</b>
        4.1. Все права на интеллектуальную собственность, связанную с ботом (включая, но не ограничиваясь, авторскими правами и товарными знаками), принадлежат владельцу бота.
        4.2. Пользователи не имеют права использовать, копировать, изменять или распространять содержимое бота без предварительного письменного согласия владельца бота.

        <b>5. Запрет на злоупотребление</b>
        5.1. Пользователям запрещено использовать бота для распространения незаконного, вредоносного или оскорбительного содержимого.
        5.2. Пользователям запрещено использовать бота для осуществления мошенничества, спама или любых других действий, которые могут повредить владельцу бота или другим пользователям.

<b>6. Изменение пользовательского соглашения</b>
        6.1. Владелец бота оставляет за собой право в любое время изменять условия данного пользовательского соглашения.
        6.2. Измененное пользовательское соглашение будет опубликовано в боте или предоставлено пользователямв виде уведомления. Пользователи обязуются периодически проверять пользовательское соглашение на наличие изменений.

<b>7. Прекращение использования</b>
        7.1. Пользователи могут прекратить использование бота в любое время.
        7.2. Владелец бота оставляет за собой право прекратить предоставление услуг пользователям в случае нарушения пользователем условий данного пользовательского соглашения или в случае несоответствия действиям пользователя законодательству или морально-этическим нормам.

<b>8. Применимое право и разрешение споров</b>
        8.1. Данное пользовательское соглашение регулируется и толкуется в соответствии с законодательством страны, в которой зарегистрирован владелец бота.
        8.2. Любые споры, возникающие между владельцем бота и пользователями, будут разрешаться путем переговоров и сотрудничества. В случае невозможности достижения согласия, споры будут переданы на рассмотрение компетентного суда.

        Пожалуйста, имейте в виду, что данное пользовательское соглашение является лишь общими правилами и условиями использования бота. Владелец бота может также иметь дополнительные политики и условия, которые могут быть доступны в боте или на его веб-сайте.
        """,
            "get_name": "Давай начнем процесс регистрации. Введи свое Ф.И.О в формате:\n\nФамилия Имя Отчество\n\nЧерез пробел!",
            "get_contact": "Отправьте контакт.",
            "error_name_format": "У вас неправильный формат❗️\n\nВведи свое Ф.И.О в формате:\n\nФамилия Имя Отчество\n\nЧерез пробел!",
            "get_location": """
Отправьте локацию 

Важное примечание нужно отравлять домашний адрес так это важно для определения точного  адреса.
                           """,
            "get_address": """
ввидите ваш адрес в формате :

Дом/кватриру/Подьезд/Этаж

Пример: 30/16/2/1
""",
            "get_comment_to_address": "Комментарии к адресу:",
            "error_address_format": """
У вас неправильный формат❗️

ввидите ваш адрес в формате :

Дом/кватриру/Подьезд/Этаж

Пример: 30/16/2/1
    """,
            "complete_registration": "Спасибо за регистрацию!",
            "error": "Что-то пошло не так❗️",
            "register_btn": "Пройти Регистрацию",
            "help_btn": "Помощь",
            "get_location_btn": "Отправить локацию",
            "get_place": "Выберите район:",
            "get_rate": """
Сейчас доступен тариф старт для выноса бытового мусора по четным и нечетным числам.  

Название тарифа "Start". 

Формат оплаты Click или Payme. 

Стоимость услуги 200.000 тыс сум( в  него входят 12 выбросов ежемесячно)

Для подтверждения оплаты вам придет уведомления об оплате в приложение.
""",
            "already_registered": "Вы уже регистрировались!",
            "profile_error": "вы ещё не регистрировались",
            "profile_btn": "Профиль",
            "create_order_btn": "Создать заказ",
            "actual_order_btn": "Актуальный заказ",
            "name_btn": "Имя",
            "house_number_btn": "номер дома",
            "apartment_number_btn": "номер квартиры",
            "entrance_number_btn": "номер подьезда",
            "floor_number_btn": "этаж",
            "comment_btn": "комментарии к адресу",
            "change_profile": "Выберите поле которое вы хотите изменить:",
            "change_name_message": "Введите новое имя:",
            "change_house_message": "Введите номер дома:",
            "change_apartment_message": "Введите номер квартиры:",
            "change_entrance_message": "Введите номер подьезда:",
            "change_floor_message": "Введите номер этажа:",
            "change_comment_message": "Введите комментарии к адресу:",
            "error_changing": "Нажмите на кнопку",
            "complete_changing": "Данные успешно изменены!",
            "confirm_btn": "Потвердить✅",
            "cancel_btn": "Отказать❌",
            "delete_btn": "Удалить аккаунт❌",
            "edit_btn": "Редакторовать профиль",
            "back_btn": "◀️Назад",
            "help_message": "link to operator @jacurlive",
            "rate_count_error": "У вас закончились количество заказов, количество оставших заказов - 0",
            "order_success": "Заказ создан - ваш остаток заказов:",
            "photo_load_error": "Ошибка при загрузке фотографии!",
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
            "deleted_success": "Аккаунт успешно удалён!",
            "accept_photo": "Отправьте фотографию пакетов возле вашей двери, что-бы курьер мог взять именно ваш заказ",
            "not_ended_order_error": "У вас есть не законченный заказ, в ближайшее время наш курьер закончит ваш заказ.Если есть проблемы нажмите на кнопку Помощь",
            "not_order_error": "У вас ещё нет актуальных заказов, нажмите на кнопку Создать заказ",
            "worker_status": "Статус курьера:",
            "order_created_time": "Время создания:",
            "order_end": "Закончен🟢",
            "order_not_end": "Незакончен🔴",
            "order_status": "Статус:",
            "default_message": "Для полной информации введите комманду /help"
        }
    }

    @staticmethod
    def get_translation(language, key):
        return Localization.translations.get(language, {}).get(key, key)
