#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
from selenium import webdriver
import common.reporter as reporter

#-----------执行时的配置信息---------------
#项目地址
sys.path.append("/Users/chenlisha/pyprojects/pytest_templete")
#配置被测环境, 值与testdata下的环境包名相同
ENV_CONFIG = "sandbox"
#配置被测浏览器
BROWSER_CONFIG = webdriver.Chrome()
#配置要执行的Run文件名(不包含后缀.py)
RUN_NAME = "run_allcase"
#--------------------------------------

if __name__ == "__main__":
    reporter.initreport()
    import_string = "run." + RUN_NAME
    mod = __import__(import_string, None, None, RUN_NAME, 0)
    mod.startrun(ENV_CONFIG, BROWSER_CONFIG)
    reportname = "rel" + RUN_NAME + "_" + time.strftime("%y%m%d%H%M%S", time.localtime()) + ".txt"  #测试报告名
    reporter.buidreport(reportname)
