#!/usr/bin/env python
from selenium import webdriver
from page import Page
import unittest, time, re
from selenium.webdriver.common.exceptions import NoSuchElementException
from run import settings

class HomePage(Page):

    _create_addon_btn = "//div[@id='features-wrapper']/div/div[1]/div[2]/div/a/span"
    _create_lib_btn = "//div[@id='libs-and-extensions']/div[3]/div[2]/div/ul/li/a/span"
    _signin_link = 'signin'
    _home_page_url = settings.HOME_PAGE_URL
    _my_account_link = "//header[@id='app-header']/div[2]/nav/ul/li[3]/span/a[1]"
    _addon_disable = "//div[@id='libs-and-extensions']/div[1]/ul[1]/li[1]/ul/li[3]/a"
    _library_disable = "//div[@id='libs-and-extensions']/div[2]/ul[1]/li[1]/ul/li[2]/a"
    _create_addon_link = "//header[@id='app-header']/div[2]/nav/ul/li[1]/div/ul/li[1]/a"
    _create_lib_link = "//header[@id='app-header']/div[2]/nav/ul/li[1]/div/ul/li[2]/a"

    def __init__(self, selenium):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = selenium

    def go_to_home_page(self):
        self.sel.get(self._home_page_url)
        self.sel.implicitly_wait(10)

    def click_signin(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        self.sel.find_element_by_id(self._signin_link).click()
        self.sel.implicitly_wait(10)
        return

#Takes you to your dashboard
    def click_myaccount(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        self.sel.find_element_by_xpath(self._my_account_link).click()
        self.sel.implicitly_wait(10)
        return

    def click_create_addon_btn(self):
        self.sel.find_element_by_xpath(self._create_addon_btn).click()
        self.sel.implicitly_wait(10)
        return

    def click_create_lib_btn(self):
        self.sel.find_element_by_xpath(self._create_lib_btn).click()
        self.sel.implicitly_wait(10)
        return

    def click_create_addon_link(self):
        self.sel.find_element_by_xpath(self._create_addon_link).click()
        self.sel.implicitly_wait(10)
        return

    def check_addon_disable_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._addon_disable)
            return True
        except NoSuchElementException:
            return False

    def check_lib_disable_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._library_disable)
            return True
        except NoSuchElementException:
            return False
