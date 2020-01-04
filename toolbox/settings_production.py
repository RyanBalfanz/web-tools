from .settings import *

PROJECT_APPS = [
	'users.apps.UsersConfig',
]

INSTALLED_APPS += [] + PROJECT_APPS

AUTH_USER_MODEL = 'users.User'
