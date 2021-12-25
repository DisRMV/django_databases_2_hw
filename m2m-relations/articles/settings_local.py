from website.settings import BASE_DIR

SECRET_KEY = 'b0e@^m&tccz11$w59qov$lhn-97!(%wfn-gray-c*x)^a$wx=3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_hw_articles',
        'USER': '',
        'PASSWORD': '',
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
