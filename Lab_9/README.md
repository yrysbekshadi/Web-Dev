# Lab 9 — Django REST Framework for Online Shop

This project upgrades Lab 8 to Django REST Framework.

## Implemented
- `djangorestframework` added to `INSTALLED_APPS`
- `CategorySerializer` and `ProductSerializer` created with `ModelSerializer`
- `CategoryViewSet` and `ProductViewSet` created with `ModelViewSet`
- custom action: `/api/categories/<id>/products/`
- `DefaultRouter` configured in `api/urls.py`
- models registered in Django admin
- database already contains **4 categories** and **20 products**
- Postman collection included: `OnlineShopAPI.postman_collection.json`

## Run
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Admin
Open: `http://127.0.0.1:8000/admin/`

Ready superuser in the attached database:
- username: `admin`
- password: `admin12345`

## API Endpoints
### Categories
- `GET /api/categories/`
- `GET /api/categories/1/`
- `GET /api/categories/1/products/`
- `POST /api/categories/`
- `PUT /api/categories/1/`
- `DELETE /api/categories/1/`

### Products
- `GET /api/products/`
- `GET /api/products/1/`
- `POST /api/products/`
- `PUT /api/products/1/`
- `DELETE /api/products/1/`
