#! /usr/bin/env python
#-*- coding: utf-8 -*-

# ***** BEGIN LICENSE BLOCK *****
# This file is part of Shelter Database.
# Copyright (c) 2016 Luxembourg Institute of Science and Technology.
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2016/05/20$"
__revision__ = "$Date: 2016/06/22 $"
__copyright__ = "Copyright (c) Luxembourg Institute of Science and Technology"
__license__ = ""

""" Program variables.

This file contain the variables used by the application.
"""

import os
import sys
import logging
try:
    import configparser as confparser
except:
    import ConfigParser as confparser

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.abspath(".")

# available languages
LANGUAGES = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German'
}

TIME_ZONE = {
    "en": "US/Eastern",
    "fr": "Europe/Paris",
    "es": "Europe/Madrid",
    "de": "Europe/Berlin"
}

DEFAULTS = {"platform_url": "http://127.0.0.1:5000",
            "host": "0.0.0.0",
            "port": "5000",
            "https": "false",
            "debug": "true",
            "secret_key": "secret_key_of_the_web_application",
            "log_path": "shelterdatabase.log",
            "log_level": "info",

            "public_path": "src/web/public",
            "shelters_pictures_path": "src/web/public/pictures/shelters",
            "shelters_documents_path": "src/web/public/documents/shelters",
            "attributes_pictures_path": "src/web/public/pictures/attributes",

            "geoserver_url": "https://shelter-database.org:8443",

            "notification_host": "",
            "notification_port": "",
            "notification_email": "",
            "notification_username": "",
            "notification_password": "",
            "notification_starttls": "true"
}

config = confparser.SafeConfigParser(defaults=DEFAULTS)
config.read(os.path.join(BASE_DIR, "conf/conf.cfg"))

PLATFORM_URL = config.get('misc', 'platform_url')

SQLALCHEMY_DATABASE_URI = config.get('database', 'database_url')

WEBSERVER_DEBUG = config.getboolean('webserver', 'debug')
WEBSERVER_HOST = config.get('webserver', 'host')
WEBSERVER_PORT = config.getint('webserver', 'port')
WEBSERVER_HTTPS = config.getboolean('webserver', 'https')
WEBSERVER_SECRET_KEY = config.get('webserver', 'secret_key')

LOG_PATH = config.get('misc', 'log_path')
LOG_LEVEL = {'debug': logging.DEBUG,
             'info': logging.INFO,
             'warn': logging.WARN,
             'error': logging.ERROR,
             'fatal': logging.FATAL}[config.get('misc', 'log_level')]

ALLOWED_EXTENSIONS_PICTURE = set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS_DOCUMENT = set(['doc', 'docx', 'pdf', 'odt', 'xls', 'xlsx',
                                    'csv'])
ALLOWED_EXTENSIONS_CSV = set(['csv'])
ALLOWED_EXTENSIONS_ARCHIVE = set(['zip'])

PUBLIC_PATH = os.path.join(PATH,
                            config.get('misc', 'public_path'))
SHELTERS_PICTURES_PATH = os.path.join(PATH,
                            config.get('misc', 'shelters_pictures_path'))
SHELTERS_DOCUMENTS_PATH = os.path.join(PATH,
                            config.get('misc', 'shelters_documents_path'))
ATTRIBUTES_PICTURES_PATH = os.path.join(PATH,
                            config.get('misc', 'attributes_pictures_path'))

GEOSERVER_URL = config.get('geoserver', 'geoserver_url')

NOTIFICATION_HOST = config.get('notification', 'notification_host')
NOTIFICATION_PORT = config.get('notification', 'notification_port')
NOTIFICATION_EMAIL = config.get('notification', 'notification_email')
NOTIFICATION_USERNAME = config.get('notification', 'notification_username')
NOTIFICATION_PASSWORD = config.get('notification', 'notification_password')
NOTIFICATION_STARTTLS = config.getboolean('notification', 'notification_starttls')

POSTMARK = False
