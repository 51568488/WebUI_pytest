#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''测试结果模块'''
import os
from os import rename
import inspect

def checkpoint(exp, des="None"):
    '''执行断言并记录到report<.txt>文件中'''
    liststack = inspect.stack()
    filename = liststack[1][1]
    if "case" in filename:   #True表示checkpoint是从case中调用
        casename = filename[filename.rfind("/")+1:len(filename)-3]
    elif "action" in filename:
        casename = liststack[2][1]
        casename = casename[casename.rfind("/")+1:len(casename)-3]
    filename = filename[filename.rfind("/")+1:]
    line = liststack[1][2]
    line = "line " + str(line)
    if exp:
        status = "Pass,"
    else:
        status = "Fail,"
    des = des + ","
    casename = casename + ","
    filename = filename + ","
    if len(status) <= 10:
        status = status.ljust(10)
    if len(casename) <= 20:
        casename = casename.ljust(20)
    if len(filename) <= 20:
        filename = filename.ljust(20)
    if len(line) <= 10:
        line = line.ljust(10)
    strlog = status + casename + filename + line + des + "\n"
    __writetempresult(strlog)

def __writetempresult(strline):
    path = os.getcwd() + "/reporter/temp.txt"
    tempresl = open(path, "a", encoding="utf-8", newline="\n")
    tempresl.writelines(strline)
    tempresl.close()

def __cleantempresult():
    path = os.getcwd() + "/reporter/temp.txt"
    tempresl = open(path, "w", encoding="utf-8", newline="\n")
    tempresl.truncate()
    tempresl.close()

def initreport():
    '''初始化测试报告'''
    status = "Status,"
    status = status.ljust(10)
    casename = "CaseName,"
    casename = casename.ljust(20)
    filename = "FileName,"
    filename = filename.ljust(20)
    line = "LineNo.,"
    line = line.ljust(10)
    strtitle = status + casename + filename + line + "Description\n"
    __cleantempresult() #清空temp.txt中的内容
    __writetempresult(strtitle)

def buidreport(reportname):
    '''生成测试报告'''
    currentname = os.getcwd() + "/reporter/temp.txt"
    newname = os.getcwd() + "/reporter/" + reportname
    rename(currentname, newname)
