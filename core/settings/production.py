#postgresql connection  
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'FDbCA6G**f2D45aEf5gD1bgab*fDa3Ff',
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT': '34284',
    }
}"""

#mongobd connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME':'api-users',
        'ENFORCE_SCHEMA': False,
        'CLIENT':{
            'host':'localhost:27017',
            'authSource': 'api-users',
        }
    }
}