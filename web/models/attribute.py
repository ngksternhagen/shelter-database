#! /usr/bin/env python
#-*- coding: utf-8 -*-

# ***** BEGIN LICENSE BLOCK *****
# This file is part of Shelter Database.
# Copyright (c) 2016
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2016/03/30$"
__revision__ = "$Date: 2016/03/30 $"
__copyright__ = "Copyright (c) "
__license__ = ""

import datetime
from sqlalchemy import desc
from bootstrap import db

class Attribute(db.Model):
    """
    Represent an attribute.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), default='')
    multiple = db.Column(db.Boolean(), default=True)
    free_text = db.Column(db.Boolean(), default=False)
    type = db.Column(db.String(), default='')
    display_position = db.Column(db.Integer, default=0)

    # relationships
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", back_populates="attributes")

    associated_values = db.relationship('Value', backref='attribute', lazy='dynamic',
                           cascade='all, delete-orphan',
                           order_by=desc('Value.id'))

    properties = db.relationship("Property", back_populates="attribute")
