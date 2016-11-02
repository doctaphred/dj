"""
Keep development settings out of the project package in order to easily
exclude them from your deployment's manifest and *completely* isolate
them from production.
"""
from dj.settings import *  # noqa

DEBUG = True
# DEBUG = False  # Uncomment for quick debugging

# Rotate secret keys to invalidate cookies and other signed data
SECRET_KEY = '1'
# SECRET_KEY = '2'
# SECRET_KEY = '3'

# Allow arbitrary passwords for development
AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# # Uncomment to use a new, semi-reasonable one-time-use secret key.
# from random import SystemRandom  # noqa
# allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# length = 50
# random = SystemRandom()
# SECRET_KEY = ''.join(random.choice(allowed_chars) for i in range(length))
# print('Using one-time-use secret key!')

# # Uncomment for extra debug info
# from pprint import pformat  # noqa
# print('Settings')
# print('========')
# for name in sorted(dir()):
#     if name.isupper() and not name.startswith('_'):
#         print('{} = {}'.format(name, pformat(vars()[name])))
# print()
