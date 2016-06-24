KEHIA Online Presence
========================
This is a https://wagtail.io/ site.

System level dependencies
---------------------------
The notes below assume that we are on Ubuntu 14.04 or 16.04.

This site depends upon the following:

 * ``memcached`` - for caching. On Ubuntu/Debian, run ``sudo apt-get install memcached``
 * ``python-all-dev`` and ``python3-all-dev``, along with ``build-essential`` - compile
   dependencies

Static files
-------------
The deployment scripts expect static files to be at ``/opt/kehiastatic``. In 
local development, of you want to be able to run ``python manage.py collectstatic``,
you need to create that folder and ensure that your shell use has read/write access
to it.

Installing and running
-------------------------
Create a virtualenv then run ``pip install -r requirements.txt``.

After that succeeds, invoke ``run`` on the command line to see the available
options.

