Deployment with Docker
======================

Prerequisites
-------------

-   Docker 1.10+.
-   Docker Compose 1.6+

Understanding the Docker Compose Setup
--------------------------------------

Before you begin, check out the `production.yml` file in the root of
this project. Keep note of how it provides configuration for the
following services:

-   `django`: your application running behind `Gunicorn`;
-   `postgres`: PostgreSQL database with the application's relational
    data;
-   `redis`: Redis instance for caching;
-   `caddy`: Caddy web server with HTTPS on by default.

Provided you have opted for Celery (via setting `use_celery` to `y`)
there are three more services:

-   `celeryworker` running a Celery worker process;
-   `celerybeat` running a Celery beat process;
-   `flower` running [Flower](https://github.com/mher/flower) (for more
    info, check out CeleryFlower instructions for local environment).

Configuring the Stack
---------------------

The majority of services above are configured through the use of
environment variables. Just check out envs and you will know the drill.

To obtain logs and information about crashes in a production setup, make
sure that you have access to an external Sentry instance (e.g. by
creating an account with [sentry.io](https://sentry.io/welcome)), and
set the `SENTRY_DSN` variable.

You will probably also need to setup the Mail backend, for example by
adding a [Mailgun](https://mailgun.com) API key and a
[Mailgun](https://mailgun.com) sender domain, otherwise, the account
creation view will crash and result in a 500 error when the backend
attempts to send an email to the account owner.

Optional: Use AWS IAM Role for EC2 instance
-------------------------------------------

If you are deploying to AWS, you can use the IAM role to substitute AWS
credentials, after which it's safe to remove the `AWS_ACCESS_KEY_ID` AND
`AWS_SECRET_ACCESS_KEY` from `.envs/.production/.django`. To do it,
create an [IAM
role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
and
[attach](https://aws.amazon.com/blogs/security/easily-replace-or-attach-an-iam-role-to-an-existing-ec2-instance-by-using-the-ec2-console/)
it to the existing EC2 instance or create a new EC2 instance with that
role. The role should assume, at minimum, the `AmazonS3FullAccess`
permission.

HTTPS is On by Default
----------------------

SSL (Secure Sockets Layer) is a standard security technology for
establishing an encrypted link between a server and a client, typically
in this case, a web server (website) and a browser. Not having HTTPS
means that malicious network users can sniff authentication credentials
between your website and end users' browser.

It is always better to deploy a site behind HTTPS and will become
crucial as the web services extend to the IoT (Internet of Things). For
this reason, we have set up a number of security defaults to help make
your website secure:

-   If you are not using a subdomain of the domain name set in the
    project, then remember to put the your staging/production IP address
    in the `DJANGO_ALLOWED_HOSTS` environment variable (see settings)
    before you deploy your website. Failure to do this will mean you
    will not have access to your website through the HTTP protocol.
-   Access to the Django admin is set up by default to require HTTPS in
    production or once *live*.

The Caddy web server used in the default configuration will get you a
valid certificate from Lets Encrypt and update it automatically. All you
need to do to enable this is to make sure that your DNS records are
pointing to the server Caddy runs on.

You can read more about this here at [Automatic
HTTPS](https://caddyserver.com/docs/automatic-https) in the Caddy docs.

(Optional) Postgres Data Volume Modifications
---------------------------------------------

Postgres is saving its database files to the `production_postgres_data`
volume by default. Change that if you want something else and make sure
to make backups since this is not done automatically.

Building & Running Production Stack
-----------------------------------

You will need to build the stack first. To do that, run:

    docker-compose -f production.yml build

Once this is ready, you can run it with:

    docker-compose -f production.yml up

To run the stack and detach the containers, run:

    docker-compose -f production.yml up -d

To run a migration, open up a second terminal and run:

    docker-compose -f production.yml run --rm django python manage.py migrate

To create a superuser, run:

    docker-compose -f production.yml run --rm django python manage.py createsuperuser

If you need a shell, run:

    docker-compose -f production.yml run --rm django python manage.py shell

To check the logs out, run:

    docker-compose -f production.yml logs

If you want to scale your application, run:

    docker-compose -f production.yml scale django=4
    docker-compose -f production.yml scale celeryworker=2

> **warning**
>
> don't try to scale `postgres`, `celerybeat`, or `caddy`.

To see how your containers are doing run:

    docker-compose -f production.yml ps

    
    
*deployment-with-docker.md is based on [deployment-with-docker.rst](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)*

