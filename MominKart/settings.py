from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()  # .env file load करने के लिए

BASE_DIR = Path(__file__).resolve().parent.parent

# ===================== Render Production Settings =====================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-e67-rjw4^u6^l+4fb5f(m@yh-8e1ibtzr31=m3y%o+hk!28s00')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# ===================== Application definition =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MominKart',  # Your app

    # Cloudinary apps
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MominKart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MominKart.wsgi.application'

# ===================== Database =======================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Can use PostgreSQL on Render later
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===================== Password validation ============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ===================== Internationalization ==========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===================== Static & Media =================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary Media Storage
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# MEDIA_URL और MEDIA_ROOT अब Cloudinary use करेगा
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Optional, mainly for local dev

# ===================== Default primary key ============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===================== Login redirect =================================
LOGIN_URL = 'user_login'
LOGIN_REDIRECT_URL = 'homepage'
