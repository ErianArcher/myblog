#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging;

logging.basicConfig(level=logging.INFO)

__author__ = 'Erian Liang'

'''
ModelMetaclass class
'''


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
