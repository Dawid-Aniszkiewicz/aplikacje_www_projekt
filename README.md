# Katalog Kwiatów – Aplikacje WWW 2026Z

Projekt zaliczeniowy z przedmiotu Aplikacje WWW. Aplikacja w Django 6.1 i Django REST Framework
do przeglądania katalogu kwiatów

Autor: Dawid Aniszkiewicz

## Wymagania

- Python 3.13+
- Git

## Uruchomienie

```bash
git clone https://github.com/Dawid-Aniszkiewicz/aplikacje_www_projekt.git
cd aplikacje_www_projekt

python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (cmd):         .venv\Scripts\activate.bat
# Linux / macOS:         source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Adresy

- http://127.0.0.1:8000/flowers/ – strona główna katalogu
- http://127.0.0.1:8000/flowers/about/ – opis aplikacji
- http://127.0.0.1:8000/admin/ – panel administracyjny