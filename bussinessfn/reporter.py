#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''测试报告相关函数'''
import os
import time
from os import rename
import inspect
import CV
import utilitytool.utjson as utjson
from json2html import json2html

def checkpoint(exp, des="None"):
    '''执行断言并记录到report文件中'''
    liststack = inspect.stack()
    filename = liststack[1][1]
    if "case" in filename:   #True表示checkpoint是从case中调用
        casename = filename[filename.rfind("/")+1:len(filename)-3]
    elif "action" in filename:
        casename = liststack[2][1]
        casename = casename[casename.rfind("/")+1:len(casename)-3]
    else:
        casename = ""
    filename = filename[filename.rfind("/")+1:]
    line = liststack[1][2]
    line = "line " + str(line)
    if exp:
        status = "Pass"
    else:
        status = "Fail"
    addresult(status, casename, filename, line, des)

def addresult(status, casename, filename, line, des):
    if CV.g_reptype == CV.FILETYPE_TXT:
        __addresult_txt(status, casename, filename, line, des)
    elif CV.g_reptype == CV.FILETYPE_JSON or CV.g_reptype == CV.FILETYPE_HTML:
        __addresult_json(status, casename, filename, line, des)

def initreport(reptype):
    '''初始化测试报告，支持html/json/txt'''
    CV.g_reptype = reptype
    __deltempresult()
    if CV.g_reptype == CV.FILETYPE_TXT:
        __initreport_txt()
    elif CV.g_reptype == CV.FILETYPE_JSON or CV.g_reptype == CV.FILETYPE_HTML:
        __writetempresult("[]")
    else:
        print("Error: 不支持的报告格式")

def buidreport(reportname = "temp"):
    '''生成测试报告'''
    if CV.g_reptype == CV.FILETYPE_HTML:
        __jsontohtml(CV.REPTMPFILE_PATH + CV.g_reptype)
    currentname = CV.REPTMPFILE_PATH + CV.g_reptype
    newname = os.getcwd() + "/reporter/" + reportname + "." + CV.g_reptype
    rename(currentname, newname)

def __initreport_txt():
    status = CV.REPFIELD_STATUS + ","
    status = status.ljust(10)
    casename = CV.REPFIELD_CASE + ","
    casename = casename.ljust(20)
    filename = CV.REPFIELD_FILE + ","
    filename = filename.ljust(20)
    line = CV.REPFIELD_LINE + ","
    line = line.ljust(10)
    strtitle = status + casename + filename + line + CV.REPFIELD_DES + "\n"
    __writetempresult(strtitle)

def __writetempresult(strline):
    path = CV.REPTMPFILE_PATH + CV.g_reptype
    with open(path, "a", encoding=CV.ENCODING, newline="\n") as tempresl:
        tempresl.writelines(strline)
        tempresl.close()

def __deltempresult():
    tmpfile = CV.REPTMPFILE_PATH + CV.g_reptype
    if os.path.exists(tmpfile):
        os.remove(tmpfile)

def __addresult_txt(status, casename, filename, line, des):
    status = status + ","
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

def __addresult_json(status, casename, filename, line, des):
    dictj = {}
    dictj[CV.REPFIELD_STATUS] = status
    dictj[CV.REPFIELD_CASE] = casename
    dictj[CV.REPFIELD_FILE] = filename
    dictj[CV.REPFIELD_LINE] = line
    dictj[CV.REPFIELD_DES] = des
    listj = utjson.loadjson(CV.REPTMPFILE_PATH + CV.g_reptype)
    listj.append(dictj)
    utjson.dumpjson(listj, CV.REPTMPFILE_PATH + CV.g_reptype)

def __jsontohtml(path):
    '''读html报告的json内容，转成html写回文件'''
    jobj = utjson.loadjson(path)
    strobj = json2html.convert(json = jobj, table_attributes=CV.REPHTML_TABLESTYLE)
    strobj = '<h1 style="text-align:center">Test Report</h1>execution timestamp:' + time.strftime("%y-%m-%d %H:%M:%S", time.localtime()) + strobj
    with open(path, "w+", encoding=CV.ENCODING, newline="\n") as tempresl:
        tempresl.truncate()
        tempresl.writelines(strobj)
        tempresl.close()
