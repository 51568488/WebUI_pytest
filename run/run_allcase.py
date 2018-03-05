#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import run.case_name_list as namelist
from common.runcase import Run

def startrun(env, browser):
    '''开始执行以下List中的case, 每个run文件必须包含些方法(方法名不可变)'''
    #------List为要执行的case name, 取至case_name_list.py------
    caselist = []
    caselist.append(namelist.CASE1)
    caselist.append(namelist.CASE2)
    #-------------------------------------------------------
    Run(env, browser, caselist)
