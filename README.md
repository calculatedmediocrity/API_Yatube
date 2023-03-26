# api_final

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/vzbdr/api_final_yatube.git
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Документация:

После запуска проекта документация для API Yatube будет доступна по адресу  http://127.0.0.1:8000/redoc/. Документация представлена в формате Redoc.
