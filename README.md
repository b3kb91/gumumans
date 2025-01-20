## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/gumumans/task-manager.git
cd task-manager

### Создать виртуальное окружение:
python -m venv venv
venv/Scripts/activate    

### 2. Установка зависимости:
pip install -r requirements.txt

### 3. Настроить БД - PostgreSQL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',  # Название вашей базы данных
        'USER': '',     # Имя пользователя базы данных
        'PASSWORD': '',  # Ваш пароль
        'HOST': 'localhost',    # Хост базы данных
        'PORT': '5432',         # Порт базы данных
    }
}

### 4. Применить миграции:
python manage.py migrate

### 5. Запустить сервер:
python manage.py runserver

### 6. url'ы для быстрого нахождения:
    - /api/task/ - главная страница для работы с задачами
    - /api/task/1/ - для CRUD определенной задачи

    - /api/auth/users/ - для аутентификации и авторизации пользователя
    - /auth/token/login/ - после авторизации получить токен юзера
    


Документация API
После запуска сервера вы можете получить доступ к документации API через Swagger.

Перейдите по адресу: http://127.0.0.1:8000/api/docs/
Все доступные эндпоинты будут отображены в интерфейсе Swagger.
