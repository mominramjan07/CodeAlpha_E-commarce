from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ===================== Render Production Settings =====================
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.onrender.com'   # Render का domain allow करने के लिए
]
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]
# ===================== Application definition =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_cloudinary_storage',  # Python 3.13 compatible
    'MominKart',  # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'ENGINE': 'django.db.backends.sqlite3',  # Or PostgreSQL on Render
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

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'django_cloudinary_storage.storage.MediaCloudinaryStorage'

# ===================== Cloudinary config ==============================
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

# ===================== Default primary key ============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===================== Login redirect =================================
LOGIN_URL = 'user_login'
LOGIN_REDIRECT_URL = 'homepage'
