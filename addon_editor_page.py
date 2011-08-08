#!/usr/bin/env python

from page import Page

class AddonEditorPage(Page):

    _addon_name = 'package-info-name'
    _signin_link = 'signin'
    _copy_btn = 'package-copy'

    def __init__(self, testsetup):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = testsetup.selenium 

    def get_addon_name(self):
        return self.sel.find_element_by_id(self._addon_name).text

    def click_signin(self):
        self.sel.find_element_by_id(self._signin_link).click()

    def click_copy_btn(self):
        self.sel.find_element_by_id(self._copy_btn).click()
