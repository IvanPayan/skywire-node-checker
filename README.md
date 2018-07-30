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

Technical documentation
----------

### Obtaining and processing data

The source of the data is http://discovery.skycoin.net:8001/conn/getAll. This source can be changed at any moment at settings/base.py changing the var API_URL.

This app uses Celery to pull every 2 minutes the data from this source.

Celery executes every 2 minutes the function autoupdate() located in utils.py inside the status_checker app.

The autoupdate() function checks first if the node with the public key exist in the database.

If not exist then creates a new node in the database and a new uptime period.

If exist could happen 3 things: 

The node is online: In that case the uptime period duration (start_time) is updated.

The node is offline: In that case the online status is set to False.

The node is online but was offline the last time that was checked: In that case, the online status is set to True and a new uptime period is created.

In all that cases when a node has been checked the last_checked log is updated.

Finally, for all the nodes that have an older last_checked log, the online status is set to False.

For the case that during this 2 minutes a node went offline and online, there is an extra control that checks that the new uptime start_time should be greater than the last log. If not, a new uptime period is created.

### Calculating uptime

The uptime % is calculated dividing the total uptime of the current month by the days passed of the current month.

For example, if during the month of June the node has changed the online status several times, the result of the total uptime will be the sum of all the periods of june plus part of the time of the last period of may that could correspond to the month of june.

The total uptime is represented in seconds.

Finally is obtained the seconds that have passed since the start of the current month. In this case following the example will be the seconds pased since 1st of June at 0:00 a.m. GMT.


How to contribute
----------
 
Check [CONTRIBUTING.md](docs/CONTRIBUTING.md)


Licence
----------

[GPLv3](LICENCE)
