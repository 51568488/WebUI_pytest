#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.action.a_login import Alogin
from src.action.a_logout import Alogout

def run_step(test_env, browser):
    '''执行本case所有步骤, 每个case文件必须包含此函数'''
    import_string = "src.testdata." + test_env + ".config"
    tcfg = __import__(import_string, None, None, "config", 0)        #导入某环境配置文件
    __clogin(tcfg.CFG_ENV_URL, browser, tcfg.CFG_SUPPLIER_USERNAME, tcfg.CFG_SUPPLIER_PASSWORD)
    __clogout(tcfg.CFG_ENV_URL, browser)

def __clogin(url, browser, username, password):
    '''登录'''
    act = Alogin(url, browser, username, password)
    act.login()

def __clogout(url, browser):
    '''登出'''
    act = Alogout(url, browser)
    act.logout()
