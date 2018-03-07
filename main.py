#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from selenium import webdriver
import bussinessfn.reporter as reporter
import bussinessfn.case as case
import CV


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
    reporter.initreport(CV.FILETYPE_TXT)
    #case.runCase(ENV_CONFIG, BROWSER_CONFIG, SUITE_NAME)
    reporter.checkpoint(1==1)
    reporter.checkpoint(1==1, "test")
    reportname = "rel_" + SUITE_NAME + "_" + time.strftime("%y%m%d%H%M%S", time.localtime()) #测试报告名
    reporter.buidreport(reportname)
