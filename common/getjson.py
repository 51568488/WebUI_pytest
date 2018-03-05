#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import os
import json

def getCaselist(suitename):
    '''取suite中的caselist'''
    path = os.getcwd() + "/suite/" + suitename + ".json"
    return __loadjson(path)   

def getData(env, filename):
    '''读取测试数据.json文件'''
    path = os.getcwd() + "/src/data/" + env + "/" + filename + ".json"
    return __loadjson(path)   

def __loadjson(path):
    load_j = open(path, 'r')
    load_dict = json.load(load_j)
    return load_dict

