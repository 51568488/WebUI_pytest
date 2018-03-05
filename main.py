#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
from selenium import webdriver
import common.reporter as reporter
import common.runcase as runcase


#-----------执行时的配置信息---------------
#项目地址
sys.path.append("/Users/chenlisha/pyprojects/pytest_templete")
#配置被测环境, 值与testdata下的环境包名相同
ENV_CONFIG = "devEnv"
#配置被测浏览器
BROWSER_CONFIG = webdriver.Chrome()
#配置要执行的suite文件名(不包含后缀.json)
SUITE_NAME = "allcase"
#--------------------------------------

if __name__ == "__main__":
    #reporter.initreport()
    runcase.Run(ENV_CONFIG, BROWSER_CONFIG, SUITE_NAME)
    #reportname = "rel" + RUN_NAME + "_" + time.strftime("%y%m%d%H%M%S", time.localtime()) + ".txt"  #测试报告名
    #reporter.buidreport(reportname)
    #getjson.getCaselist(SUITE_NAME)
