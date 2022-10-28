from config.settings.base import *  # noqa

CURRENT_ENV = "DEV"
print(CURRENT_ENV)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)
STATIC_URL = "static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        },
    }
else:
    DATABASES = {
        "default_sql": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
        "default_local": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "bizon",
            "USER": "postgres",
            "PASSWORD": "admin",
            "HOST": "localhost",
            "PORT": "5432",
        },
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        },
    }
