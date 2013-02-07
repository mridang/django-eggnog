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

There isn't much else than that to get it up and running.
