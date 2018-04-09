#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import os
import time
import json
import CV
import utilitytool.utjson as utjson
import bussinessfn.reporter as reporter



def RunSuite(reptype = None):
    '''执行指定suite, 执行每个case文件的run_step()函数
    reptype = CV.FILETYPE_TXT/CV.FILETYPE_JSON/CV.FILETYPE_HTML
    '''
    if CV.ENV_CONFIG == None or CV.SUITE_NAME == None or CV.BROWSER == None:
        print("Error: 未配置“ENV_CONFIG/SUITE_NAME/BROWSER”")
    elif reptype == None:
        __RunCase()
    else:
        reporter.initreport(reptype)
        __RunCase()
        reportname = "rel_" + CV.SUITE_NAME + "_" + time.strftime("%y%m%d%H%M%S", time.localtime()) #测试报告名
        reporter.buidreport(reportname)       

def __RunCase():
    caselist_j = __getCaselist()
    for key in caselist_j:
        import_string = "src.case." + caselist_j[key]
        mod= __import__(import_string, None, None, caselist_j[key], 0)  # import要执行的case模块
        mod.run_step()  # 执行该模块的run_step()函数

def __getCaselist():
    '''取suite中的caselist'''
    path = os.getcwd() + "/suite/" + CV.SUITE_NAME + "." + CV.FILETYPE_JSON
    return utjson.loadjson(path)   