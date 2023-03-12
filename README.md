# Пульт охраны банка
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
___
### Описание:
Это внутренний репозиторий для сотрудников банка "Сияния". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к `Базе Данных`, но можете использовать код вёрстки или посмотреть как реализованы запросы к `Базе Данных`.
Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.
___
>### Для запуска программы требуется:
 * скачать [Python](https://www.python.org/) версии 3.1 или выше.
 * операционная система macOS, linux, windows 7 или выше.
 * установить все нужные библиотеки Python командой:
```
pip install -r requirements.txt
```
___
>### Как запустить программу:
* #### Укажите переменные окржения:
    Программа берет настройки из нестандартных переменных окружения. Перед запуском программы создаём фаил .env, туда положите:
    * ENGINE=django.db.backends.postgresql_psycopg2
    * HOST=host
    * PORT=port
    * NAME=name
    * USER=user
    * PASSWORD=password
    * SECRET_KEY=secret_key
    * ROOT_URLCONF = root_urlconf
    * DEBUG=False
* Для запуска программы требуется, написать в консоль команду:
```
python manage.py runserver 0.0.0.0:8000
```
* После того как программа запуститься, нужно перейти по ссылке этого сайта:
```
127.0.0.1:8000
```
___
>### Цель проекта:
* Код написан в образовательных целях 