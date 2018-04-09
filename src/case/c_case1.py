#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.action.a_login import Alogin
import bussinessfn.reporter as reporter
import bussinessfn.testdata as tdata
import CV

def run_step():
    '''执行本case所有步骤, 每个case文件必须包含此函数''' 
    #--------配置执行时调用的action函数------------
    __clogin()
    #------------------------------------------

def __clogin():
    '''登录'''
    data_j = tdata.getData("config")
    act = Alogin(data_j["url"], data_j["username"], data_j["password"])
    act.login()
    reporter.checkpoint(True, "case1 pass")
    

