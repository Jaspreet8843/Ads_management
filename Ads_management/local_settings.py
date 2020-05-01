#py manage.py runserver --settings=Ads_management.local_settings
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'janambhumi',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

SECURE_SSL_REDIRECT = False
