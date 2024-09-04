### Немного теории

* С помощью создания папки `.venv` и команды `pipenv install django==4.0.8` наша виртуальная среда устанавливается именно туда, вдобавок создается два фала - `Pipfil` и `Pipfile.lock`

* `pipenv shell` и `pip list` - мы активируем виртуальную среду и выводим список фалов или же можно применить `pipenv graph`просто она более красивый вид умеет 

* Выйти из подобного режима можно с помощью команды `exit`

* `pip list` - список всех установленных пакетов

* `sudo pip install name_of_package` - позволяет устанавливать что-либо

* `sudo pip uninstall name_of_package` - позволяет удалять что-либо

* `sudo install pipenv` - новый инструмент 

* `pipenv --venv` - показывает путь до виртуальной среды, тем самым мы свзяываем имнно нашу виртуальную среду и все установленные зависимости, чтобы не было ошибок и прочего

### Команды Django

* `django-admin startproject name_of_project .` - команда для django для создания проекта, причём папка определяется как пакет, поскольку имеет файл `__init__`

* `python manage.py runserver` - запускает сервер Django

* `python manage.py migrate` - создаем и мигрируем базы данных

* `python3 manage.py createsuperuser` - можем создать суперпользователя

* `python3 manage.py makemigrations` - создаем и мигрируем новые модели, которые мы создаем для баз данных после чего ->
* `python manage.py migrate` - создаем и мигрируем базы данных

* `python3 manage.py shell` - жуткий режим когда работаешь из-под встроенной оболочки

* `python manage.py startapp api`