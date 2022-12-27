from .comman import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dragontesting01.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dragontesting01$dragonstore',
        'HOST': 'dragontesting01.mysql.pythonanywhere-services.com',
        'USER': 'dragontesting01',
        'PASSWORD': 'Brucelee47'
    }
}
