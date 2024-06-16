Трекер привычек на основе описания выработки привычек из книги Джеймса Клира «Атомные привычки»
Проект представляет собой трекер привычек, основанный на принципах, описанных в книге Джеймса Клира «Атомные привычки».

Установка и настройка

Клонирование репозитория:
git clone https://github.com/Arctiqa/drf-course.git

Создайте файл .env в корне проекта и установите необходимые переменные окружения:

SECRET_KEY=your_secret_key
DEBUG=True/False

POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db_host
POSTGRES_PORT=db_port

TELEGRAM_TOKEN=your_telegram_token
CELERY_BROKER_URL=celery_broker_url
CELERY_RESULT_BACKEND=celery_result_backend
TIME_ZONE=your_time_zone

Используйте docker-compose для создания и запуска контейнеров:
docker-compose up -d --build
