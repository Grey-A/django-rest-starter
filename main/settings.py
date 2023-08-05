import os

if os.environ.get("DJANGO_ENV") == "PRODUCTION":
    from .production_settings import *
else:
    from .production_settings import *
