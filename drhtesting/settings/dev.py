from .comman import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-hf88ovdliw1$#!dqsu2j24m60%2=+frf(6&0wtkn=hrq%4sii$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

    }
}
