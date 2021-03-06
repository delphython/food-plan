# Сервис FoodPlan

Роман и Лариса долго и слюбовью копили рецепты, которыми готовы поделиться с Вами! Конструктор подписки поможет выбрать тип меню, количество приемов пищи и даже учесть пищевые аллергии.

Попробуйте демо-версию сайта по [ссылке](http://82.148.16.182/).

![](/static/demo.png)

## Источники данных

Тестовые данные взяты с сайта [Поваренок](https://www.povarenok.ru/). В проекте реализована команда для парсинга данных с сайта.

## Хочу такой же

Исходный код доступен для скачивания в данном репозитории GitHub. Чтобы запустить сайт у себя на компьютере, понадобится:

- Скачайте код или воспольуйтесь `git clone`
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных `db.sqlite3` и сразу примените все миграции командой `python3 manage.py migrate`
- Создайте учетную запись администратора базы данных командой `python manage.py createsuperuser`
- Запустите сервер командой `python3 manage.py runserver`
- Доступ к сайту по адресу [127.0.0.1:8000](http://127.0.0.1:8000/), админка доступна по адресу [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

Через админку создавайте рецпты блюд, загружайте фотки и смотрите результаты на сайте! Для автоматизированной загрузки данных перейдите в раздел "Загрузка данных в базу".

## Настройки

В проекте используются следующие переменные окружения:
- `DEBUG` — флаг режима отладки. Поставьте `False` для боевого сервера. Если не указан, то True.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте. Не стоит использовать значение по-умолчанию, **замените на своё**.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `DATABASE_URL` - конфигурация БД, указывается в виде URL, см. [примеры](https://github.com/jacobian/dj-database-url#id7). Если значение не указано, то используется движок `SQLite`, имя файла `db.sqlite`. Для использования `PostgreSQL` в `requirements.txt` добавлена библиотека [psycorg2](https://pypi.org/project/psycopg2/).
- `YOOKASSA_SHOP_TOKEN`, `YOOKASSA_SHOP_ID` - для авторизации в платежной системе [Юmoney](https://yoomoney.ru/)

## Используемые библиотеки

* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Django](https://www.djangoproject.com/start/) — серверная часть сайта, включая модель данных на Django ORM
* [environs](https://pypi.org/project/environs/) v загрузка переменных окружения
* [Pillow](https://pypi.org/project/Pillow/) — обработка изображений, используется для ImageField в моделях
* [dj-database-url](https://pypi.org/project/dj-database-url/) — парсинг URL базы данных
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - парсинг рецептов с сайта [Поваренок](https://www.povarenok.ru/)
* [yookassa](https://pypi.org/project/YooMoney/) - интеграция с платежной системой [Юmoney](https://yoomoney.ru/)

## Кастомизированная админка

Административный интерфейс сайта позволяет:
- Установить цены для конструктора подписки
- Создавать новые блюда
- Деактивировать блюда, чтобы они не предлагадись пользователям
- Анализировать статистику по платежам в зависимости от типа меню

![](/static/admin_demo.png)

## Загрузка данных в базу

Чтобы спарсить и загрузить в базу тестовые данные с сайта [Поваренок](https://www.povarenok.ru/) выполните команду:
```bash
python manage.py parsing_recipes_website
```

## Цели проекта

Код написан в учебных целях — это командный проект в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
