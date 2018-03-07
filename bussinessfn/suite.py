#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import os
import json
import CV
import utilitytool.utjson as utjson

def getCaselist(suitename):
    '''取suite中的caselist'''
    path = os.getcwd() + "/suite/" + suitename + ".json"
    return utjson.loadjson(path)   