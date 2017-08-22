#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import logging; logging.basicConfig(level=logging.INFO)
import aiomysql

__author__ = 'Erian Liang'

'''
Base class of models
'''

class Model(dict, metaclass=ModelMetaclass):
