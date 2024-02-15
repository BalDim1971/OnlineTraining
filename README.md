# Онлайн-обучение
# DRF

## Задание к уроку 24.1

В мире развивается тренд на онлайн-обучение. Но для веб-разработчика важно не 
только обучиться, но и знать, как реализовать платформу для онлайн-обучения. 
Поэтому новая задача касается разработки LMS-системы, в которой каждый желающий
может размещать свои полезные материалы или курсы.

Ранее в проектах мы могли сразу видеть визуальное отображение результата 
разработки, теперь работа будет над SPA веб-приложением и результатом создания 
проекта будет бэкенд-сервер, который возвращает клиенту JSON-структуры.

### Задание 1
Создайте новый Django-проект, подключите DRF в настройках проекта.

### Задание 2
Создайте следующие модели:

1. Пользователь:
- все поля от обычного пользователя, но авторизацию заменить на email;
- телефон;
- город;
- аватарка.

Модель пользователя разместите в приложении users

2. Курс:
- название,
- превью (картинка),
- описание.

3. Урок:
- название,
- описание,
- превью (картинка),
- ссылка на видео.

Урок и курс - это связанные между собой сущности. Уроки складываются в курс, 
в одном курсе может быть много уроков. 
Реализуйте связь между ними.

Модель курса и урока разместите в отдельном приложении. Название для приложения
выбирайте такое, чтобы оно описывало то, с какими сущностями приложение 
работает. Например, lms или materials - отличные варианты.

### Задание 3
Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса 
используйте Viewsets, а для урока - Generic-классы.

Для работы контроллеров опишите простейшие сериализаторы.

При реализации CRUD для уроков реализуйте все необходимые операции 
(получение списка, получение одной сущности, создание, изменение и удаление).

Работу каждого эндпоинта необходимо проверять с помощью Postman.
Также на данном этапе работы мы не заботимся о безопасности и не закрываем от 
редактирования объекты и модели даже самой простой авторизацией.


## Задание к уроку 24.2

Продолжаем развивать проект LMS системы для более удобной работы с ним.

### Задание 1
Для модели курса добавьте в сериализатор поле вывода количества уроков. 
Поле реализуйте с помощью SerializerMethodField()

### Задание 2
Добавьте новую модель в приложение users:

1. Платежи
- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.

Поля пользователь, оплаченный курс и отдельно оплаченный урок
должны быть ссылками на соответствующие модели.

Запишите в таблицу, соответствующую этой модели данные через инструмент 
фикстур или кастомную команду.

Если вы забыли как работать с фикстурами или кастомной командой - можете 
вернуться к уроку 20.1 "Работа с ORM в Django" чтобы вспомнить материал.

### Задание 3
Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод 
реализуйте с помощью сериализатора для связанной модели.

Один сериализатор должен выдавать и количество уроков курса и информацию 
по всем урокам курса одновременно.

### Задание 4
Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:
- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

#### Дополнительное задание
Для профиля пользователя сделайте вывод истории платежей, расширив 
сериализатор для вывода списка платежей

### Критерии решения:
Результат выполнения всего задания залит в github.com и сдан в виде ссылки 
на репозиторий
Примечание: дополнительные задания помеченные звездочкой желательны, но 
не обязательны к выполнению.


Описание работ для PyCharm в Windows.

1. Создать и активировать виртуальное окружение.
python -m venv venv
.\venv\Scripts\activate

2. Установить зависимости проекта, указанные в файле requirements.txt
pip install -r requirements.txt 
или средствами PyCharm.

3. Создать файл .env.
Записать в файл настройки, как в шаблоне .env.sample

Применить миграции

python manage.py migrate users
python manage.py migrate

Создать суперпользователя
python manage.py csu

Для тестового прогона можно использовать файл test.json:
python mange.py loaddata test.json

Запустить сервер
python manage.py runserver
