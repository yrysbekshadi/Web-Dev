# Lab 10: Building API Views

This project refactors the Lab 9 shop-back API using multiple DRF view patterns.

## Implemented levels
- `api/views/fbv.py` — function-based views for products
- `api/views/cbv.py` — class-based API views for products
- `api/views/mixins.py` — mixin-based views for products
- `api/views/generics.py` — generic views for products and categories
- `api/views/__init__.py` — currently activates Level 5 (`generics.py`)

## Active endpoints
- `GET, POST /api/categories/`
- `GET, PUT, DELETE /api/categories/<id>/`
- `GET /api/categories/<id>/products/`
- `GET, POST /api/products/`
- `GET, PUT, DELETE /api/products/<id>/`

## Run
```bash
python manage.py runserver
```
