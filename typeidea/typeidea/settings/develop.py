# flake: NOQA
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "typeidea",
        'USER':'root',
        'PASSWORD':"12345678",
        'HOST':'127.0.0.1',
        'PORT':3306,
    }
}