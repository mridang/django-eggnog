from pkg_resources import *

from django.db import models

class Update(models.Model):
    """
    Model for storing the updates
    """
    package = models.CharField(max_length=2000, null=False, unique=True)
    installed = models.CharField(max_length=16, null=False)
    available = models.CharField(max_length=16, null=False)
    checked = models.DateTimeField(auto_now_add=True, null=False)

    def __unicode__(self):
        """
        String representation method.
        """
        return self.package + ' [' + self.installed + ']'

    class Meta:
        """
        Meta.
        """
        ordering = ['-checked']

    def updateable(self):
        """
        Custom property indicating whether an update is available.
        """
        return True if parse_version(self.installed) < parse_version(self.available) else False

    updateable.boolean = True

    def cheeseshop(self):
        """
        Returns a URL pointing to the package on PyPi
        """
        return '<a href="http://pypi.python.org/pypi/%s/">%s</a>' % (self.package, self.package)

    cheeseshop.allow_tags = True
