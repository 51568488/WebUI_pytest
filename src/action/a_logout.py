#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

class Alogout(object):
    '''登出 参数:无'''

    def __init__(self, url, browser):
        self.url = url
        self.driver = browser

    def logout(self):
        '''注销(不关闭浏览器)'''
        driver = self.driver
        logout_url = self.url + "logout"
        driver.get(logout_url)
        time.sleep(3)
