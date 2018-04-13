#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from selenium import webdriver
import bussinessfn.suite as suite
import utilitytool.utelement as utelement
from src.action.a_login import Alogin
import CV



#-----------执行时的配置信息---------------
#项目地址
sys.path.append("/Users/chenlisha/pyprojects/pytest_templete")
#配置被测环境, 值与testdata下的环境包名相同
CV.ENV_CONFIG = "devEnv"
#配置被测浏览器
CV.BROWSER = webdriver.Chrome()
#配置要执行的suite文件名(不包含后缀.json)
CV.SUITE_NAME = "allcase"
#--------------------------------------

if __name__ == "__main__":
    suite.RunSuite()
    #act = Alogin("http://dev.go.xltec.cc/", "wumao_admin", "123456")
    #act.login()
    #utelement.createObjfile()

