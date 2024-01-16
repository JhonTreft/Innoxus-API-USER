from .config_vars import BASE_DIR   

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'bd/db.sqlite3',
    }
}





