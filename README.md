Skywire Node Checker
==================

<p align="center">
<img src="https://www.skycoin.net/static/media/logo.d3da7a19.svg" width="200">
</p>

Skywire, the distributed Internet of Skycoin has been conceived with the purpose of becoming a freer, safer, faster and cheaper alternative to the Internet that works on the old infrastructure of cables and antennas built by the ISP's, usually large multinational telecommunications companies, that control the ability of each individual to be able to communicate with another.

This alternative seeks to create a new infrastructure of small antennas built by individuals who can communicate with each other and at the same time give Internet access to those people who wish to connect and who are close to an antenna.

To incentivize the initiative of individuals to invest in the construction of this infrastructure, Skywire is backed by a third-generation cryptocurrency called Skycoin. This means that anyone who decides to install a node (known as Skywire miner) in their home and provides high availability of it, will receive a monthly return on Skycoins.

But to be qualified to receive the monthly return there is only one condition: keep the active node at least 75% of the time on a monthly basis.

For this purpose I have created and now I make this tool available to the community so that any individual can control the activity of their nodes in a simple way.

<br>
<p align="center">
<img src="/docs/skywire_node_checker.png" width="900">
</p>

Settings
--------

See detailed [settings](docs/settings.md).

Technology
----------

Django (2.0.7) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Built by experienced developers, it takes care of much of the hassle of Web development,
so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

Django 2.0.7 only works with [Python 3](https://www.python.org/downloads/)

More info [Django project](https://docs.djangoproject.com/).
More info [Phython](https://www.python.org/).

Development
----------
### Locally

        $ python manage.py runserver

See detailed [Development Locally](docs/developing-locally.md)

### Docker (Recomended option)

    $ docker-compose -f local.yml up
   
See detailed [Development Docker](docs/developing-locally-docker.md)

Basic Commands
--------------

### Setting Up Your Users

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    $ py.test

### Live reloading and Sass CSS compilation

    $ npm run dev

See detailed [Live reloading and SASS compilation](docs/live-reloading-and-sass-compilation.md)

### Celery

This app comes with Celery.

To run a celery worker:

``` {.sourceCode .bash}
cd skywire_node_checker
celery -A skywire_node_checker.taskapp worker -l info
```

To run a celery scheduler task:
``` {.sourceCode .bash}
cd skywire_node_checker
celery -A skywire_node_checker.taskapp beat -l info
```

Please note: For Celery's import magic to work, it is important *where*
the celery commands are run. If you are in the same folder with
*manage.py*, you should be right.

See detailed [Celery](docs/installing_celery.md).

Deployment
----------

The following details how to deploy this application.

### Docker

You will need to build the stack first. To do that, run:

    docker-compose -f production.yml build

Once this is ready, you can run it with:

    docker-compose -f production.yml up

To run the stack and detach the containers, run:

    docker-compose -f production.yml up -d

See detailed [Deployment with Docker](docs/deployment-with-docker.md).


### Backups


To create a backup, run:

    $ docker-compose -f production.yml exec postgres backup

See detailed [Docker PostgresSQL Backups](docs/docker-postgres-backups.md).

How to contribute
----------
 
Check [CONTRIBUTING.md](docs/CONTRIBUTING.md)


Licence
----------

[GPLv3](LICENCE)
