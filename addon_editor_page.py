#!/usr/bin/env python
import settings

from selenium import selenium
from selenium import webdriver
from page import Page

class AddonEditorPage(Page):

    _addon_name = 'package-info-name'
    _signin_link = 'signin'
    _home_page_url = settings.HOME_PAGE_URL
    _copy_btn = 'package-copy'

    def __init__(self, testsetup):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = testsetup.selenium 

    def get_addon_name(self):
        return self.sel.find_element_by_id(self._addon_name).text

    def click_signin(self):
        self.sel.find_element_by_id(self._signin_link).click()
        return

    def click_copy_btn(self):
        self.sel.find_element_by_id(self._copy_btn).click()
        self.sel.implicitly_wait(10)
        return
