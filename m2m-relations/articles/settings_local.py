import os
from website.settings import BASE_DIR

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_hw_articles',
        'USER': os.getenv('USER_DB'),
        'PASSWORD': os.getenv('PASS_DB'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }
