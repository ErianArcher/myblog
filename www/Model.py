#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from www.orm import Model, IntegerField, StringField

__author__ = 'Erian Liang'

'''
User Model
'''


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()