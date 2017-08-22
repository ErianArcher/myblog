#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging;

from www.Field import Field

logging.basicConfig(level=logging.INFO)

__author__ = 'Erian Liang'

'''
StringField class
'''

class StringField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)