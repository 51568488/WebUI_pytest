#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import os
import json
import CV
import utilitytool.utjson as utjson

def getData(filename):
    '''读取测试数据.json文件'''
    path = os.getcwd() + "/src/tdata/" + CV.ENV_CONFIG + "/" + filename + "." + CV.FILETYPE_JSON
    return utjson.loadjson(path)   