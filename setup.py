# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '1.0.0.dev0'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='cmcuritiba.portalmodelo.theme',
    version=version,
    description='Tema da Camara Municipal de Curitiba',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='diazo theme',
    author='Forcontent',
    author_email='andre@forcontent.com.br',
    url='CHANGES.rst',
    license='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['cmcuritiba', 'cmcuritiba.portalmodelo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.themingplugins',
        'plone.resource',
        'Products.CMFPlone >=4.3',
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.theming',
            'plone.registry',
            'plone.testing',
            'transaction',
            'zope.component',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)