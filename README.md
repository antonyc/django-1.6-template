# mydjangoproject

This is a [project
template](https://docs.djangoproject.com/en/1.6/ref/django-admin/#startproject-projectname-destination)
for Django 1.6, ideal for a stack/workflow/environment setup that includes
PostgreSQL, virtualenv/virtualenvwrapper, OS X, Fabric, and Heroku.


## Installation

1. Create a root directory under `~/repos` or wherever you store your code

1. Create a virtualenv and activate it

1. Install Django with pip:

        pip install django==1.6

1. Create the project using this template from the zipball (note the `.` at the
end of the command so that there won't be too many nested repositories):

        django-admin.py startproject --template=https://github.com/ysim/django-1.6-template/archive/master.zip mydjangoproject .

1. Remove this section once you're done with the next section (Setup).


## Setup

Be sure to go through this entire section before making your initial commit.

* If you're on OS X >= 10.7, consider installing
[Postgres.app](http://postgresapp.com/). Then follow [the
instructions](http://postgresapp.com/documentation) to (most importantly) add
the `bin/` dir of the Postgres.app to your $PATH.

* With the virtualenv activated, install the requirements via pip:

        $ pip install -r requirements.txt

* Create a new role, as well as the `_dev` and `_test` databases in Postgres:

        $ psql
        psql (9.3.1)
        Type "help" for help.

        ysim=# CREATE ROLE yiqing WITH LOGIN PASSWORD 'yiqing' CREATEDB;
        CREATE ROLE
        ysim=# CREATE DATABASE mydjangoproject_dev OWNER yiqing;
        CREATE DATABASE
        ysim=# CREATE DATABASE mydjangoproject_test OWNER yiqing;
        CREATE DATABASE

* Create database tables and define a superuser:

        $ ./manage.py syncdb
        Creating tables ...
        Creating table django_admin_log
        Creating table auth_permission
        Creating table auth_group_permissions
        Creating table auth_group
        Creating table auth_user_groups
        Creating table auth_user_user_permissions
        Creating table auth_user
        Creating table django_content_type
        Creating table django_session

        You just installed Django's auth system, which means you don't have any superusers defined.
        Would you like to create one now? (yes/no): yes
        Username (leave blank to use 'ysim'): 
        Email address:
        Password: 
        Password (again): 
        Superuser created successfully.
        Installing custom SQL ...
        Installing indexes ...
        Installed 0 object(s) from 0 fixture(s)

* Run `fab generate_secret_key` to, well, generate a secret key and modify
`.postactivate` to reflect the new secret key.

* Optionally, specify a different port for the Django development server to
run on in the `serve` task of the fabfile.

* Append `.postactivate` to `.gitignore`.

* Make the `setup` script executable, then execute it (it renames all instances
of `mydjangoproject` to your new project name):

        $ chmod +x setup
        $ ./setup


## Run the development server

        $ fab serve


## Troubleshooting

You might encounter an error while installing psycopg2:

        Error: pg_config executable not found.

        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:

        python setup.py build_ext --pg-config /path/to/pg_config build ...

        or with the pg_config option in 'setup.cfg'.
        Complete output from command python setup.py egg_info:
        running egg_info

    creating pip-egg-info/psycopg2.egg-info

    writing pip-egg-info/psycopg2.egg-info/PKG-INFO

    writing top-level names to pip-egg-info/psycopg2.egg-info/top_level.txt

    writing dependency_links to pip-egg-info/psycopg2.egg-info/dependency_links.txt

    writing manifest file 'pip-egg-info/psycopg2.egg-info/SOURCES.txt'

    warning: manifest_maker: standard file '-c' not found



    Error: pg_config executable not found.



    Please add the directory containing pg_config to the PATH

    or specify the full executable path with the option:



    python setup.py build_ext --pg-config /path/to/pg_config build ...



    or with the pg_config option in 'setup.cfg'.

To solve this, temporarily append the `bin/` folder under the Postgres
application to your $PATH and re-run the pip install command, e.g.

    PATH="$PATH:/Applications/Postgres93.app/Contents/MacOS/bin/" pip install psycopg2


## References

* <http://kennethreitz.org/repository-structure-and-python/>
