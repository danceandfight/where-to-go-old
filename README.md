# Куда пойти — Москва глазами Артёма

## Как пользоваться

* Сайт доступен по ссылке: 
* Админка доступна по ссылке (необходимы логин и пароль!):

Если необходимо добавить на сайт новые места или внести правки в существующие сделайте следующее:
1. Перейдите в админку по ссылке выше
2. Перейдите в список локаций (places)
3. Если нужно найти определенную локацию, посмотрите в появившемся списке (или используйте строку поиска)
4. Если нужно создать новую локацию нажмите `Add place +` справа вверху

Если хотите поработать с сайтом, сделайте следующее:

1. Скачайте репозиторий
2. Перейдите в папку проекта в командной строке и установите зависимости командой: `pip install -r requirements.txt`
3. Примените миграции к сайту командой: `python manage.py migrate`
4. Запустите сайт командой: `python manage.py runserver`. Сайт будет доступен в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/), админка по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
Если видите в консоли сообщение: `System check identified no issues (0 silenced)`
5. Через админку наполните сайт данными: 

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
