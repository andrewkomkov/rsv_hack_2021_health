Реализованная сейчас функциональность

Макет фронтенда для работы эксперта;
REST API для интеграции сейчас доступен в яндекс облаке по эндпоинтам:
https://functions.yandexcloud.net/d4er0l7m5u7cblpob6n5
https://functions.yandexcloud.net/d4e5famsggvkmu73p07p
Документация и принцип работы описаны в документе:
тех_api.docx


Особенность проекта в следующем:
Умная система помощи в принятии решения по оценке оказанных медицинских услуг
Возможность интеграции с любой Медицинской системой
Может найти аномалию даже среди случая который проходит по нормативной документации

Основной стек технологий:

Python/Django
Django

Демо сервиса доступно по адресу: https://app.komkov.tk/life_checker_app/r/#

СРЕДА ЗАПУСКА

Развертывание сервиса производится на debian-like linux (ubuntu 20.04);

УСТАНОВКА django

https://www.digitalocean.com/community/tutorialshow-to-install-the-django-web-framework-on-ubuntu-18-04-ru


Старт сервиса:

Необходимо перейти в директорию проекта:
cd rsv_life_checker_project
и выполнить: 
python manage.py runserver

После этого сервис станет доступен по ссылке:
http://127.0.0.1:8000/life_checker_app/r/

РАЗРАБОТЧИКИ

Иванов Иван fullstack https://t.me/test@name1