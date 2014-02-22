# mydjangoproject


## Setup

* If you're on OS X >= 10.7, consider installing
[Postgres.app](http://postgresapp.com/). Then follow [the
instructions](http://postgresapp.com/documentation) to (most importantly) add
the `bin/` dir of the Postgres.app to your $PATH.

* Create a virtualenv, activate it, and install the pip requirements:

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

* Run the `setup` script to rename all instances of `mydjangoproject` to your
new project name.


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
