#coding:utf-8

import importlib

import mod_a


del(mod_a.b)
mod_a.a=0


importlib.reload(mod_a)

from pprint import pprint

pprint(mod_a.__dict__)