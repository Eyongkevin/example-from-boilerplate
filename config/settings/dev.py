from .base import *

import environs

# SET UP variable environment
env = environs.Env()

env.read_env(str(BASE_DIR / '.env'))

SECRET_KEY = env.str('SECRET_KEY')


DEBUG = True

ALLOWED_HOSTS = []


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # needs `pip install "psycopg[binary]"`
        "NAME": env.str("DB_NAME"),  # database name
        "USER": env.str("DB_USER"),  # database user
        "PASSWORD": env.str("DB_PWD"),  # database password
        # "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}