# Import the original settings from each template
from .basesettings import *

try:
    from .local_settings import LOCAL_DATABASE
except ImportError:
    pass

# Pulling django-environ settings file, stored in Secret Manager
import environ
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file = os.path.join(BASE_DIR, ".env")

SETTINGS_NAME = "application_settings"
AUTH_USER_MODEL = "backoffice.User"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "backoffice.customAuthentification.customAuthentification",
)

if not os.path.isfile(".env"):
    import google.auth
    from google.cloud import secretmanager_v1beta1 as sm

    _, project = google.auth.default()

    if project:
        client = sm.SecretManagerServiceClient()
        path = client.secret_version_path(project, SETTINGS_NAME, "latest")
        payload = client.access_secret_version(path).payload.data.decode("UTF-8")

        with open(env_file, "w") as f:
            f.write(payload)

env = environ.Env()
env.read_env(env_file)

# Setting this value from django-environ
SECRET_KEY = env("SECRET_KEY")

# Could be more explicitly set (see "Improvements")
ALLOWED_HOSTS = ["*"]

# Default false. True allows default landing pages to be visible
DEBUG = env("DEBUG")

# Setting this value from django-environ
try:
    DATABASES = LOCAL_DATABASE
except NameError:
    DATABASES = {"default": env.db()}

INSTALLED_APPS += ["storages"]  # for django-storages
if "bm_back" not in INSTALLED_APPS:
    INSTALLED_APPS += ["bm_back"]  # for custom data migrationclear

# Define static storage via django-storages[google]
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
STATICFILES_DIRS = []
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_DEFAULT_ACL = "publicRead"
