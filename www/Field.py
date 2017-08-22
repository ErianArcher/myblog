#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging;

logging.basicConfig(level=logging.INFO)

__author__ = 'Erian Liang'

'''
Field class
'''


class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)
