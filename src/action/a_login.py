#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import src.object.o_login
import src.object.o_tasklist
from common.reporter import checkpoint

class Alogin(object):
    '''参数:url, username, passowrd'''

    def __init__(self, url, browser, username, password):
        self.username = username
        self.password = password
        self.url = url
        self.driver = browser

    def login(self):
        '''登录'''
        driver = self.driver
        driver.implicitly_wait(60)
        driver.get(self.url)
        obj = src.object.o_login
        input_username = driver.find_element_by_name(obj.INPUT_USERNAME_NAME)
        input_username.clear()
        input_username.send_keys(self.username)
        input_password = driver.find_element_by_name(obj.INPUT_PASSWORD_NAME)
        input_password.clear()
        input_password.send_keys(self.password)
        driver.find_element_by_name(obj.BUTTON_LOGIN_NAME).click()
        time.sleep(3)
        #检查登录跳转正确
        obj = src.object.o_tasklist
        element_user = driver.find_element_by_id(obj.DIV_USER_ID)
        checkpoint(element_user != None, "检查用户登录是否成功")
