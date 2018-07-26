Sass Compilation & Live Reloading
=================================

If you\'d like to take advantage of live reloading and Sass / Compass
CSS compilation you can do so with a little bit of prep work.

Make sure that [nodejs] is installed. Then in the project root run:

    $ npm install

If you don\'t already have it, install compass (doesn\'t hurt if you run
this command twice):

    gem install compass

Now you just need:

    $ npm run dev

The base app will now run as it would with the usual
`manage.py runserver` but with live reloading and Sass compilation
enabled.

To get live reloading to work you\'ll probably need to install an
[appropriate browser extension]

  [nodejs]: http://nodejs.org/download/
  [appropriate browser extension]: http://livereload.com/extensions/
pandoc 2.2.1

© 2013–2015 John MacFarlane

*live-reloading-and-sass-compilation.md is based on [live-reloading-and-sass-compilation.rst](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html)*

