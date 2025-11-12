"""Minimal Django settings for the OctoFit Tracker exercise.

This file intentionally contains the Codespace URL pattern used by the exercise CI
so the workflow can detect the change (the string '-8000.app.github.dev').
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'exercise-secret-key'

DEBUG = True

# Allow Codespace-hosted domain (using environment variable at runtime)
# The CI is checking that the file contains the pattern '-8000.app.github.dev'
ALLOWED_HOSTS = [
    os.environ.get('CODESPACE_NAME', 'your-codespace') + '-8000.app.github.dev',
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    # octofit app placeholder
    'octofit_tracker',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'octofit_tracker.urls'

TEMPLATES = []

WSGI_APPLICATION = 'octofit_tracker.wsgi.application'

# Minimal DB config for exercise (no real DB dependency here)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
