#!/usr/bin/env python
import os
import sys
import argparse
from django.conf import settings


class QuickDjangoTest(object):
    """
    A quick way to run the Django test suite without a fully-configured project.

    Example usage:

        >>> QuickDjangoTest('app1', 'app2')

    Based on a script published by Lukasz Dziedzia at:
    http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
    """

    DIRNAME = os.path.dirname(__file__)
    INSTALLED_APPS = ()

    def __init__(self, *args, **kwargs):
        self.apps = args
        self.run_tests()

    def run_tests(self):
        """
        Fire up the Django test suite
        """
        settings.configure(
            ROOT_URLCONF="multi_email_field.tests",
            DEBUG=True,
            DATABASES={
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": os.path.join(self.DIRNAME, "database.db"),
                    "USER": "",
                    "PASSWORD": "",
                    "HOST": "",
                    "PORT": "",
                }
            },
            MIDDLEWARE_CLASSES=(
                "django.contrib.sessions.middleware.SessionMiddleware",
                "django.middleware.common.CommonMiddleware",
                "django.middleware.csrf.CsrfViewMiddleware",
                "django.contrib.auth.middleware.AuthenticationMiddleware",
                "django.contrib.messages.middleware.MessageMiddleware",
            ),
            DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
            INSTALLED_APPS=self.INSTALLED_APPS + self.apps,
        )
        import django

        django.setup()
        from django.test.runner import DiscoverRunner

        failures = DiscoverRunner().run_tests(self.apps, verbosity=1)
        if failures:  # pragma: no cover
            sys.exit(failures)


if __name__ == "__main__":
    """
    What do when the user hits this file from the shell.

    Example usage:

        $ python quicktest.py app1 app2

    """
    parser = argparse.ArgumentParser(
        usage="[args]", description="Run Django tests on the provided applications."
    )
    parser.add_argument("apps", nargs="+", type=str)
    args = parser.parse_args()
    QuickDjangoTest(*args.apps)
