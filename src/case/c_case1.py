#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.action.a_login import Alogin
import common.getjson as getjson

def run_step(env, browser):
    '''执行本case所有步骤, 每个case文件必须包含此函数''' 
    #--------配置执行时调用的action函数------------
    __clogin(env, browser)
    #------------------------------------------

def __clogin(env, browser):
    '''登录'''
    data_j = getjson.getData(env, "config")
    act = Alogin(data_j["url"], browser, data_j["username"], data_j["password"])
    act.login()

