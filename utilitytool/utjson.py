#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import os
import json
import CV

def loadjson(path):
    '''指定文件地址，读取.json文件，返回Dir类型'''
    jobj = json.load(open(path, 'r', encoding=CV.ENCODING))
    jobj = json.dumps(jobj)
    dictobj = json.loads(jobj)
    return dictobj

def dumpjson(dirobj, path):
    '''指定文件地址，写入.json文件'''
    json.dump(dirobj, open(path, 'w', encoding=CV.ENCODING), ensure_ascii=False)



    

