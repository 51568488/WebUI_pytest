#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from selenium import webdriver
import bussinessfn.reporter as reporter
import bussinessfn.suite as suite
import CV
import utilitytool.utmysql as utmysql


#-----------执行时的配置信息---------------
#项目地址
sys.path.append("/Users/chenlisha/pyprojects/pytest_templete")
#配置被测环境, 值与testdata下的环境包名相同
ENV_CONFIG = "devEnv"
#配置被测浏览器
#BROWSER_CONFIG = webdriver.Chrome()
#配置要执行的suite文件名(不包含后缀.json)
SUITE_NAME = "allcase"
#--------------------------------------

if __name__ == "__main__":
    '''
    reporter.initreport()
    suite.runCase(ENV_CONFIG, BROWSER_CONFIG, SUITE_NAME)
    reportname = "rel_" + SUITE_NAME + "_" + time.strftime("%y%m%d%H%M%S", time.localtime()) #测试报告名
    reporter.buidreport(reportname)
    '''
    typeid = ('001',)
    res = utmysql.queryFirstRow("""select * from tmp_rule where datatypeid = %s""", typeid)
    print(res)

