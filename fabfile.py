from fabric.api import local
from fabric.context_managers import lcd


def serve():
    """ Run the development server """
    local('./manage.py runserver 0.0.0.0:8000')


def test(*apps):
    """ Usage: fab test:app_name1[,app_name2] """
    if len(apps) > 0:
        for app in apps:
            print "\n\nTesting the '%s' app..." % app
            local('./manage.py test %s --settings=mydjangoproject.settings.test' % app)
    else:
        print "Please specify at least one app."


def generate_secret_key():
    from random import choice
    print ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        for i in range(50)])


def pip_upgrade_all():
    """
    Upgrade all packages with pip.
    Source: http://stackoverflow.com/a/17689760/1094541
    """
    local("for package in `pip list | awk -F ' ' '{print $1}'` ; "
        "do pip install -U $package ; done")
    local("pip freeze >| ../requirements.txt")
