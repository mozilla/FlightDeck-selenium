#!/usr/bin/env python

from selenium.webdriver.common.by import By
from page import Page

class DashboardPrivatePage(Page):

    _top_private_addon_name = "//section[@id='app-content']/ul/li[1]/h3"
    _top_private_lib_name = "//section[@id='app-content']/ul/li[1]/h3"
    _addon_mkpublic_btn = "//section[@id='app-content']/ul/li[1]/ul/li[3]/a"
    _lib_mkpublic_btn_locator = (By.XPATH, "//a[@title='Let the world use it']")
    _my_account_link = (By.XPATH, "//a[@title='My Account']")

    def __init__(self, testsetup):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = testsetup.selenium

    def get_top_addon_name(self):
        return self.sel.find_element_by_xpath(self._top_private_addon_name).text
    
    def get_top_lib_name(self):
        return self.sel.find_element_by_xpath(self._top_private_lib_name).text
        
    def click_addon_mkpublic_btn(self):
        self.sel.find_element_by_xpath(self._addon_mkpublic_btn).click()
        self.sel.implicitly_wait(10)
        return
    
    def click_lib_mkpublic_btn(self):
        self.sel.find_element(*self._lib_mkpublic_btn_locator).click()
        self.sel.implicitly_wait(10)
        return
    
    def go_to_dashboard(self):
        self.sel.find_element(*self._my_account_link).click()
        self.sel.implicitly_wait(10)
        return
