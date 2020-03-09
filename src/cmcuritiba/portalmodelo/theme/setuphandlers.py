# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):  # pragma: no cover

    def getNonInstallableProfiles(self):
        """Return a list of non-installable profiles."""
        return [
        ]


def post_install(context):
    """Post install script."""

