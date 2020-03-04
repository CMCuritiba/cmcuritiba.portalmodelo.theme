# -*- coding: utf-8 -*-
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import cmcuritiba.portalmodelo.theme
        self.loadZCML(package=cmcuritiba.portalmodelo.theme)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'plone.app.theming:default')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name='cmcuritiba.portalmodelo.theme:Integration')

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name='cmcuritiba.portalmodelo.theme:Functional')
