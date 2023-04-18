# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    #    'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'dentist_main', 
    #    'HOST': 'localhost',
    #    'USER': 'root',
    #    'PASSWORD': 'Root@@5Henk!',

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
