# codex_test

Proyecto base de API TODO usando Django y Django Rest Framework.

## Características

- CRUD de tareas mediante API REST.
- Ganchos para integraciones con Google Calendar, WhatsApp, Slack y Notion.
- Base de datos SQLite por defecto.

## Requisitos

- Python 3.11
- Dependencias listadas en `requirements.txt`.

## Uso rápido

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Las integraciones externas son solo placeholders y deben implementarse con las credenciales correspondientes.
