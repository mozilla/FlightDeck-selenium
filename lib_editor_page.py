#!/usr/bin/env python

from selenium import webdriver
from page import Page

class LibraryEditorPage(Page):

    _library_name = 'package-info-name'
    _copy_btn = 'package-copy'
    

    def __init__(self, selenium):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = selenium

    def get_lib_name(self):
        return self.sel.find_element_by_id(self._library_name).text

    def click_copy_btn(self):
        self.sel.find_element_by_id(self._copy_btn).click()
        self.sel.implicitly_wait(10)
        return
