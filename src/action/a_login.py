#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import src.object.o_login
import CV
import utilitytool.utelement as utelement
import src.object.o_index

class Alogin(object):
    '''参数:url, username, passowrd'''

    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url
        self.driver = CV.BROWSER

    def login(self):
        '''登录'''
        driver = self.driver
        driver.get(self.url)
        obj = src.object.o_login
        input_username = driver.find_element_by_id(obj.INPUT_USERNAME_ID)
        input_username.send_keys(self.username)
        input_password = driver.find_element_by_id(obj.INPUT_PASSWORD_ID)
        input_password.send_keys(self.password)
        driver.find_element_by_xpath(obj.BUTTON_SUBMIT_XPATH).click()
        driver.find_element_by_xpath(obj.SUBMIT_ANTBTNCLICKED_XPATH).click()
        driver.implicitly_wait(5)
        obj = src.object.o_index
        driver.find_element_by_xpath(obj.BUTTON_INVOICEENTRY_XPATH).click()
        utelement.createObjfile()

