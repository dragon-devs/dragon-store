from .comman import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dragonstore',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Brucelee47'
    }
}