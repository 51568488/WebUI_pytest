#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

FILETYPE_TXT = "txt"
FILETYPE_JSON = "json"
FILETYPE_HTML = "html"

ENCODING = "utf-8"

REPFIELD_STATUS = "Status"
REPFIELD_CASE = "CaseName"
REPFIELD_FILE = "FileName"
REPFIELD_LINE = "Line No."
REPFIELD_DES = "Description"
REPTMPFILE_PATH = os.getcwd() + "/reporter/temp."
REPHTML_TABLESTYLE = 'font-family: verdana,arial,sans-serif;font-size:11px;color:#333333;border-width: 1px;border-color: #666666;border-collapse: collapse;'

OBJFOLDER_PATH = os.getcwd() + "/src/object/"

MYSQL_CONN_HOST = "116.62.207.246"
MYSQL_CONN_POST = 36544
MYSQL_CONN_USERNAME = "kxldevtest"
MYSQL_CONN_PWD = "kJds66MBJsnsa92"
MYSQL_CONN_DBNAME = "kxl_dev_db"
MYSQL_CONN_CHARSET = 'utf8mb4'

global REPTPYE
REPTPYE = None
global ENV_CONFIG
ENV_CONFIG = None
global SUITE_NAME
SUITE_NAME = None
global BROWSER
BROWSER = None


