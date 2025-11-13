#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Load local env vars from env.py if present (env.py is in .gitignore)
    try:
        import env  # sets local environment variables like SECRET_KEY
    except Exception:
        # env.py isn't required; continue if it's missing
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codestar.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
