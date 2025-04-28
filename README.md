# Django Tree Menu

A Django app for creating dynamic tree-like menus using template tags.

## Features

- Menus are stored in the database.
- Editing through Django Admin.
- Draws menu by name with `{% draw_menu 'menu_name' %}`.
- Active menu item is detected by the current URL.
- Supports multiple menus on the same page.
- Only one database query per menu rendering.
- Uses only Django and the Python standard library.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MaskedGod/django_menu.git
cd django_menu
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
```

3. Install dependencies:

```bash
pip install Django
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

---

## Usage

1. Go to the Django Admin panel (`/admin`).
2. Create a new `Menu` (e.g., "main_menu").
3. Add `MenuItems`, specifying:
   - Title
   - URL or Named URL
   - Parent (optional)
   - Menu (select the menu you created)

4. In your templates, load and draw the menu:

```django
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```

---

## Requirements

- Python 3.10+
- Django 5.2+

---

## Project Structure

```sh
menu_project/
├── menu_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── menus/                         # Приложение для меню
│       ├── migrations/
│       ├── templates/
│       │   ├── menus/                 # Шаблоны тегов меню
│       │   │   └── menu_template.html
│       ├── __init__.py
│       ├── admin.py                   # Настройки админки
│       ├── apps.py
│       ├── models.py                  # Модели меню
│       ├── templatetags/              # Кастомные теги шаблонов
│       │   ├── __init__.py
│       │   └── menu_tags.py           # Тег draw_menu
│       ├── urls.py                    # URL-ы приложения
│       └── views.py                   # Представления
├── db.sqlite3
└── manage.py
```
