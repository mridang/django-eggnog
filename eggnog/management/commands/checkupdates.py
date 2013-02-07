from threading import Thread
from pkg_resources import *

from django.core.management.base import BaseCommand, CommandError

from yolk.setuptools_support import get_pkglist
from yolk.yolklib import get_highest_version, Distributions
from yolk.pypi import CheeseShop

from eggnog.models import Update

class Command(BaseCommand):
    """
    Custom management command for checking for package updates.
    """
    help = 'Checks for package updates from PyPi'

    threads = []
    dists = Distributions()
    pypi = CheeseShop()

    def __init__(self, *args, **kwargs):
        """
        Initializer for the management commands to flush stale data.
        """
        super(Command, self).__init__(*args, **kwargs)

        Update.objects.all().delete()

    def handle(self, *args, **options):
        """
        Main management command method that starts the checking process.
        """
        print "Checking for updates from PyPi"

        for pkg in get_pkglist():

            for (dist, active) in self.dists.get_distributions("all", pkg, self.dists.get_highest_installed(pkg)):
                 thread = Thread(target=self.__check_pypi, args=(dist.project_name, dist.version))
                 self.threads.append(thread)
                 thread.start()

        for thread in self.threads:
            thread.join()

    def __check_pypi(self, name, current):
        """
        Queries PyPi for updates
        """
        (package, versions) = self.pypi.query_versions_pypi(name)

        if versions:
            newest = get_highest_version(versions)
            if newest != current:
                if parse_version(current) < parse_version(newest):
                    print " * Updates for %s are available. You have %s and the latest is %s." % (package, current, newest)
                else:
                    print " * No updates are available for %s." % (package) 
            Update.objects.create(package=package, installed=current, available=newest)
                
