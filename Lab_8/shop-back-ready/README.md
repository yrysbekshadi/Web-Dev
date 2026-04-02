# Lab 8 — Django backend for Online Shop

This project matches the lab requirements:
- project package: `shop_back`
- app: `api`
- models: `Category`, `Product`
- JSON endpoints under `/api/`

## Run

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Add data in admin
Open `http://127.0.0.1:8000/admin/` and add categories/products.

Suggested categories from your Lab 5:
- Смартфоны
- Наушники
- Компьютеры
- Ноутбуки

## Endpoints
- `/api/products/`
- `/api/products/1/`
- `/api/categories/`
- `/api/categories/1/`
- `/api/categories/1/products/`
```
