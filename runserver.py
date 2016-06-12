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
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2016/03/30$"
__revision__ = "$Date: 2016/06/06 $"
__copyright__ = "Copyright (c) "
__license__ = ""

from bootstrap import conf, app, manager, populate_g
from web import models

with app.app_context():
    populate_g()

    # HTML views
    from web import views
    app.register_blueprint(views.user_bp)
    app.register_blueprint(views.shelter_bp)
    app.register_blueprint(views.shelters_bp)
    app.register_blueprint(views.admin_bp)

    # API
    from web import processors
    # 'User' Web service
    blueprint_user = manager.create_api_blueprint(models.User,
                        methods=['GET', 'POST', 'PUT', 'DELETE'],
                        preprocessors=dict(
                                POST=[processors.auth_func,
                                    processors.shelter_POST_preprocessor],
                                DELETE=[processors.auth_func]))
    app.register_blueprint(blueprint_user)

    # 'Shelter' Web service
    blueprint_shelter = manager.create_api_blueprint(models.Shelter,
                        methods=['GET', 'POST', 'PUT', 'DELETE'],
                        preprocessors=dict(
                                POST=[processors.auth_func,
                                    processors.shelter_POST_preprocessor],
                                DELETE=[processors.auth_func]))
    app.register_blueprint(blueprint_shelter)

    # 'ShelterPicture' Web service
    blueprint_shelter_picture = manager.create_api_blueprint(models.ShelterPicture,
                        methods=['GET', 'POST', 'PUT', 'DELETE'])
    app.register_blueprint(blueprint_shelter_picture)

    # 'Category' Web service
    blueprint_category = manager.create_api_blueprint(models.Category,
                        methods=['GET', 'POST', 'PUT', 'DELETE'])
    app.register_blueprint(blueprint_category)

    # 'Attribute' Web service
    blueprint_attribute = manager.create_api_blueprint(models.Attribute,
                        methods=['GET', 'POST', 'PUT', 'DELETE'])
    app.register_blueprint(blueprint_attribute)

    # 'AttributePicture' Web service
    blueprint_attribute_picture = manager.create_api_blueprint(models.AttributePicture,
                        methods=['GET', 'POST', 'PUT', 'DELETE'])
    app.register_blueprint(blueprint_attribute_picture)

    # 'Value' Web service
    blueprint_value = manager.create_api_blueprint(models.Value,
                        methods=['GET', 'POST', 'PUT', 'DELETE'])
    app.register_blueprint(blueprint_value)

    # 'Property' Web service
    blueprint_property = manager.create_api_blueprint(models.Property,
                        methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                        preprocessors=dict(
                                POST=[processors.auth_func],
                                DELETE=[processors.auth_func]))
    app.register_blueprint(blueprint_property)

    # 'Page' Web service
    blueprint_page = manager.create_api_blueprint(models.Page,
                        methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
    app.register_blueprint(blueprint_page)

    # 'Translation' Web service
    blueprint_translation = manager.create_api_blueprint(models.Translation,
                        methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
    app.register_blueprint(blueprint_translation)


if __name__ == "__main__":
    app.run(host=conf.WEBSERVER_HOST,
                    port=conf.WEBSERVER_PORT,
                    debug=conf.WEBSERVER_DEBUG)
