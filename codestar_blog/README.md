# codestar_blog

Minimal Django 4.2 project scaffold that serves `Hello, blog!` at `/blog/`.

Setup (Windows, bash):

```bash
# create & activate virtualenv
python -m venv .venv
source .venv/Scripts/activate

# install dependencies
pip install -r requirements.txt

# run migrations and start server
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Visit http://127.0.0.1:8000/blog/ to see the message.

Notes:
- .venv is added to .gitignore; don't commit it.
- This project uses SQLite for simplicity.
