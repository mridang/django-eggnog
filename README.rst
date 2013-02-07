============
django-eggnog
============

View all available updates for your installed eggs right from within the administration console. 

Eggnog is a simple wrapper on Yolk. Eggnog works best when it is scheduled to run at a periodic internal. It fetches the list of installed eggs and quries PyPI for any available updates.

If there's a feature that you're missing and you'd like added, please create an issue on the project page at Github or create the fix yourself and send me a pull request. Adding a few small features here and there are okay but this is in no way aimed to encompass all the functionality of a full-blown package management tool like Pip.

Installation
======================

Grab the latest release from PyPI by running::

	pip install django-eggnog

Please note that this requires Django 1.3+ to work properly.

Configuration
======================

Add ``eggnog`` to your project's ``INSTALLED_APPS`` setting and run ``syncdb`` (or ``migrate`` if you're using South).

``django-eggnog`` relies on the ``apscheduler`` module to provide the periodical checks for updates. In order to configure this, please add the following two lines to your ``urls.py``::

    import eggnog
    eggnog.periodicallycheckforupdates()

If you have a very small Django installation, I suggest you stick with this but if you wish to not use ``apscheduler``, disregard the above step and uninstall ``apscheduler`` by running::

    pip uninstall apscheduler

There isn't much else than that to get it up and running.

Scheduling
==========

Eggnog works best when it is shcheduled to run at periodic intervals. Checking for updates once a day is quite enough.

Eggnog has a management-command built-in caleed ``checkupdates`` that it relies on to check for updates and here a few ways that that you can use to schedule it:

- Cron: You can configure cron to execute the management command once a day using this:    
  ``* * * * * cd /home/path/to/project && python manage.py checkupdates``


- Use a package like ``django-kronos`` or ``django-chrnonograph``. Both the Django modules . once configured . make it extremely simple schedule management-commands using cron. They are both available on PyPI and you should consult their documentation on further instructions.


- Celery: If your Django project already deals with distributed task queues, it's extremely likely that you're using ``django-celery``. In that case, configure ``django-celery`` to execute ``checkupdates`` periodically. Explaining the configuration of ``django-celery`` is outside the scope of this document.

- APScheduler: ``APScheduler`` is is an extremely lightweight module to running tasks periodically within Python. This is what ``django-eggnog`` ships with.
