import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = os.environ.get("SECRET_KEY", "AarB8<11Yx8TMr+@u>4(D+P|3")
DEBUG = os.environ.get("DEBUG", default=False)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/staticfiles/"
