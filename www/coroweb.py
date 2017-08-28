#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import inspect

__author__ = 'Erian Liang'

'''
JSON API definition
'''


def get(path):
    '''
    Define decorator @get('/path')
    :param path:
    :return:
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator


def post(path):
    '''
    Define decorator @post('/path')
    :param path:
    :return:
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind == inspect.Paramter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)