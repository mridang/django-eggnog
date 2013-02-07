import sys
from setuptools import setup, find_packages

setup(
    name = "django-eggnog",
    package_data = {
        'eggnog': [
            'README.rst',
            'LICENSE.txt',
        ],
    },
    author = "Mridang Agarwalla",
    author_email = "mridang.agarwalla@gmail.com",
    maintainer = "Mridang Agarwalla",
    maintainer_email = "mridang.agarwalla@gmail.com",
    download_url='http://github.com/mridang/django-eggnog/downloads',
    bugtrack_url='http://github.com/mridang/django-eggnog/issues',
    description = "Displays available egg updates from PyPi",
    long_description=open('README.rst').read(),
    url = "http://github.org/mridang/django-eggnog",
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages = [
        'eggnog',
        'eggnog.migrations',
        'eggnog.management.commands',
    ],
    zip_safe = True,
    license = "BSD License",
    install_requires = [
        'Django>=1.4',
        'south>=0.7.2',
        'yolk',
        'apscheduler',
    ],
    version = '0.0.1',
)
