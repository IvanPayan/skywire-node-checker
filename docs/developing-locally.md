Getting Up and Running Locally
==============================

Setting Up Development Environment
----------------------------------

Make sure to have the following on your host:

-   [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/);
-   pip;
-   PostgreSQL ([install instructions](installing_postgres.md)).

First things first.

1.  [Create a
    virtualenv](https://virtualenv.pypa.io/en/stable/userguide/).
2.  Activate the virtualenv you have just created.
3.  Install development requirements: :

        $ pip install -r requirements/local.txt

4.  Create a new PostgreSQL database (note: if this is the first time a
    database is created on your machine you might need to alter a
    localhost-related entry in your `pg_hba.conf` so as to utilize
    `trust` policy): :

        $ createdb skywire_node_checker

5.  Apply migrations: :

        $ python manage.py migrate

6.  See the application being served through Django development server:
    :

        $ python manage.py runserver 0.0.0.0:8000

Sass Compilation & Live Reloading
---------------------------------

If you’d like to take advantage of live reloading and Sass / Compass CSS
compilation you can do so with a little bit of
[preparation](live-reloading-and-sass-compilation.md).

Summary
-------

Congratulations, you have made it! Keep on reading to unleash full
potential of Skywire Node Checker.

*developing-locally.md is based on [developing-locally.rst](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)*
