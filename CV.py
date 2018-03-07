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

global g_reptype


