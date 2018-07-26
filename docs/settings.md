Settings
========

This project relies extensively on environment settings which **will not
work with Apache/mod\_wsgi setups**. It has been deployed successfully
with both Gunicorn/Nginx and even uWSGI/Nginx.

For configuration purposes, the following table maps environment
variables to their Django setting and project settings:



  | Environment Variable                        | Django Setting         | Development Default   | Production Default|
  | ------------------------------------------- |:----------------------:|:---------------------:| ----------------: |
  | DJANGO\_READ\_DOT\_ENV\_FILE                | READ\_DOT\_ENV\_FILE   | False                 | False             |

  | Environment Variable                        | Django Setting                   | Development Default             | Production Default|
  | ------------------------------------------- |:--------------------------------:|:-------------------------------:| ----------------: |
  | DJANGO\_ADMIN\_URL                          | n/a                              | 'admin/'                        | raises error      |
  | DJANGO\_CACHES                              | CACHES (default)                 | locmem                          | redis             |
  | DJANGO\_DATABASES                           |  DATABASES (default)             | See code                        | See code          |
  | DJANGO\_DEBUG                               | DEBUG                            | True                            | False
  | DJANGO\_SECRET\_KEY                         | SECRET\_KEY                      | !!!SET DJANGO\_SECRET\_KEY!!!   | raises error
  | DJANGO\_SECURE\_BROWSER\_XSS\_FILTER        | SECURE\_BROWSER\_XSS\_FILTER     | n/a                             | True
  | DJANGO\_SECURE\_SSL\_REDIRECT               | SECURE\_SSL\_REDIRECT            | n/a                             | True
  | DJANGO\_SECURE\_CONTENT\_TYPE\_NOSNIFF      | SECURE\_CONTENT\_TYPE\_NOSNIFF   | n/a                             | True
  | DJANGO\_SECURE\_FRAME\_DENY                 | SECURE\_FRAME\_DENY              | n/a                             | True
  | DJANGO\_SECURE\_HSTS\_INCLUDE\_SUBDOMAINS   | HSTS\_INCLUDE\_SUBDOMAINS        | n/a                             | True
  | DJANGO\_SESSION\_COOKIE\_HTTPONLY           | SESSION\_COOKIE\_HTTPONLY        | n/a                             | True
  | DJANGO\_SESSION\_COOKIE\_SECURE             | SESSION\_COOKIE\_SECURE          | n/a                             | False
  | DJANGO\_DEFAULT\_FROM\_EMAIL                | DEFAULT\_FROM\_EMAIL             | n/a                             | "your\_project\_name \<<noreply@your_domain_name>\>"
  | DJANGO\_SERVER\_EMAIL                       | SERVER\_EMAIL                    | n/a                             | "your\_project\_name \<<noreply@your_domain_name>\>"
  | DJANGO\_EMAIL\_SUBJECT\_PREFIX              | EMAIL\_SUBJECT\_PREFIX           | n/a                             | "[your\_project\_name] "
  | DJANGO\_ALLOWED\_HOSTS                      | ALLOWED\_HOSTS                   | ['\*']                          | ['your\_domain\_name']

The following table lists settings and their defaults for third-party
applications, which may or may not be part of your project:

  | Environment Variable                 | Django Setting               | Development Default   | Production Default|
  | ------------------------------------ |:----------------------------:|:---------------------:| ----------------: |
  | DJANGO\_AWS\_ACCESS\_KEY\_ID         | AWS\_ACCESS\_KEY\_ID         | n/a                   | raises error
  | DJANGO\_AWS\_SECRET\_ACCESS\_KEY     | AWS\_SECRET\_ACCESS\_KEY     | n/a                   | raises error
  | DJANGO\_AWS\_STORAGE\_BUCKET\_NAME   | AWS\_STORAGE\_BUCKET\_NAME   | n/a                   | raises error
  | MAILGUN\_API\_KEY                    | MAILGUN\_ACCESS\_KEY         | n/a                   | raises error
  | MAILGUN\_DOMAIN                      | MAILGUN\_SENDER\_DOMAIN      | n/a                   | raises error
  | NEW\_RELIC\_APP\_NAME                | NEW\_RELIC\_APP\_NAME        | n/a                   | raises error
  | NEW\_RELIC\_LICENSE\_KEY             | NEW\_RELIC\_LICENSE\_KEY     | n/a                   | raises error


Project Settings
--------------------------

  | Project Variable                     | Definition
  | ------------------------------------ |:----------------------------:|
  | API_URL                              | URL of the Discovery online node list       
  | MIN_UPTIME_PERCENT                   | Minimum uptim percentage (75% by default)   
  | GOOGLE_ANALYTICS_ID                  | User id for google analytics 
 


Other Environment Settings
--------------------------

DJANGO\_ACCOUNT\_ALLOW\_REGISTRATION (=True)
:   Allow enable or disable user registration through django-allauth
    without disabling other characteristics like authentication and
    account management. (Django Setting: ACCOUNT\_ALLOW\_REGISTRATION)


*settings.md is based on [settings.rst](http://cookiecutter-django.readthedocs.io/en/latest/settings.html)*
