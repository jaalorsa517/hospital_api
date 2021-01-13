from os import environ

postgres_db = environ.get('POSTGRES_DB')
postgres_user = environ.get('POSTGRES_USER')
postgres_password = environ.get('POSTGRES_PASSWORD')
postgres_host = environ.get('POSTGRES_HOST')