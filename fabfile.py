from os.path import dirname, abspath
import os
from fabric.api import local
from fabric.api import lcd

BASE_DIR = dirname(abspath(__file__))
BACKEND_PROJECT_ROOT = os.path.join(BASE_DIR, '')
FRONTEND_PROJECT_ROOT = os.path.join(BASE_DIR, '')


def run():
    local('{}/manage.py runserver 8001'.format(BACKEND_PROJECT_ROOT))


def setup(*args, **kwargs):
    with lcd(BACKEND_PROJECT_ROOT):
        local('rm db.sqlite3')
        local('python manage.py syncdb ')


def load():
    with lcd(BACKEND_PROJECT_ROOT):
        local('python manage.py loaddata data/data.json')
        local('python manage.py loaddata data/locations.json')
        local('python manage.py loaddata data/industries.json')
        local('python manage.py loaddata data/organizations.json')
        local('python manage.py loaddata data/contact_type.json')
        local('python manage.py loaddata data/contacts.json')
        local('python manage.py loaddata data/organization_contact.json')

