#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import os
import json
import CV
import utilitytool.utjson as utjson

def getCaselist(suitename):
    '''取suite中的caselist'''
    path = os.getcwd() + "/suite/" + suitename + "." + CV.FILETYPE_JSON
    return utjson.loadjson(path)   

def runCase(env, browser, suitename):
    '''执行指定suite, 执行每个case文件的run_step()函数'''
    caselist_j = getCaselist(suitename)
    for key in caselist_j:
        import_string = "src.case." + caselist_j[key]
        mod= __import__(import_string, None, None, caselist_j[key], 0)  # import要执行的case模块
        mod.run_step(env, browser)  # 执行该模块的run_step()函数