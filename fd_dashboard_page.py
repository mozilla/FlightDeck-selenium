#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#                 Zac Campbell
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from fd_base_page import FlightDeckBasePage
from page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DashboardPage(FlightDeckBasePage):

    _page_title = "Dashboard - Add-on Builder"

    _public_addons_link = (By.LINK_TEXT, "Public Add-ons")
    _public_libraries_link = (By.LINK_TEXT, "Public Libraries")
    _private_addons_link = (By.LINK_TEXT, "Private Add-ons")
    _private_libraries_link = (By.LINK_TEXT, "Private Libraries")
    _confirm_delete_btn = (By.ID, 'delete_package')
    _addons_public_counter = (By.ID, "public_addons_no")
    
    def addon(self, arg):
        return self.Addon(self.testsetup, arg)

    def library(self, index):
        return self.Library(self.testsetup, arg)
        
    @property
    def addons_count_label(self):
        return self.selenium.find_element(*self._addons_public_counter).text

    def addons_element_count(self):
        return self.addon(None).element_count
        
    def click_private_addons_link(self):
        self.selenium.find_element(*self._private_addons_link).click()
    
    def click_private_libraries_link(self):
        self.selenium.find_element(*self._private_libraries_link).click()
    
    def click_public_libraries_link(self):
        self.selenium.find_element(*self._public_libraries_link).click()

    def confirm_delete(self):
        self.selenium.find_element(*self._confirm_delete_btn).click()

    class Addon(Page):
    
        def __init__(self, testsetup, arg):
            Page.__init__(self, testsetup)
            self.arg = arg
 
        _addon = (By.XPATH, "//ul[preceding-sibling::h2[text()='Your Latest Add-ons']][1]")
        _ui_item = (By.CSS_SELECTOR, "li.UI_Item")

        _name = (By.CSS_SELECTOR, "h3:not(span)")
        _version = (By.CSS_SELECTOR, "h3 > span.version")

        _test_btn = (By.CSS_SELECTOR, "li.UI_Try_in_Browser > a")  
        _edit_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a") 
        _delete_btn = (By.CSS_SELECTOR, "li.UI_Delete > a")
        _public_btn = (By.CSS_SELECTOR, "li.UI_Activate > a")
        _private_btn = (By.CSS_SELECTOR, "li.UI_Disable > a")
     
        @property
        def root_locator(self):
            ul = self.selenium.find_element(*self._addon)
            
            if type(self.arg) is int:
                return ul.find_elements(*self._ui_item)[self.arg - 1]
            elif type(self.arg) is unicode:
                return ul.find_element(By.XPATH, "//li[child::h3[contains(text(),'%s')]]" % self.arg)

        def is_present(self):
            return self.root_locator.is_displayed()

        @property
        def element_count(self):
            ul = self.selenium.find_element(*self._addon)
            return len(ul.find_elements(*self._ui_item))

        @property
        def name(self):
            # here we are stripping the <span class="version">
            # text from the h3 to get *just* the addon's name
            name = self.root_locator.find_element(*self._name).text
            version = self.root_locator.find_element(*self._version).text
            return str(name).replace(version, "").rstrip()    
            
        def click_test(self):
            self.root_locator.find_element(*self._test_btn).click()

        def click_edit(self):
            self.root_locator.find_element(*self._edit_btn).click()
            
        def click_delete(self):
            self.root_locator.find_element(*self._delete_btn).click()
            
        def click_public(self):
            self.root_locator.find_element(*self._public_btn).click()
            
        def click_private(self):
            self.root_locator.find_element(*self._private_btn).click()

    class Library(Page):
    
        def __init__(self, testsetup, index):
            Page.__init__(self, testsetup)
            self.index = index - 1
           
        _library = (By.XPATH, "//ul[preceding-sibling::h2[text()='Your Latest Libraries']][1]")
        _ui_item = (By.CSS_SELECTOR, "li.UI_Item")
    
        _name = (By.CSS_SELECTOR, "h3:not(span)")
        _version = (By.CSS_SELECTOR, "h3 > span.version")
        _edit_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a") 
        _delete_btn = (By.CSS_SELECTOR, "li.UI_Delete > a")
        _public_btn = (By.CSS_SELECTOR, "li.UI_Activate > a")
        _private_btn = (By.CSS_SELECTOR, "li.UI_Disable > a")
     
        @property
        def root_locator(self):
            ul = self.selenium.find_element(*self._library)
            
            if type(self.arg) is int:
                return ul.find_elements(*self._ui_item)[self.arg - 1]
            elif type(self.arg) is unicode:
                return ul.find_element(By.XPATH, "//li[child::h3[contains(text(),'%s')]]" % self.arg)

        def is_present(self):
            return self.root_locator.is_displayed()

        @property
        def element_count(self):
            ul = self.selenium.find_element(*self._addon)
            return len(ul.find_elements(*self._ui_item))

        @property
        def name(self):
            # here we are stripping the <span class="version">
            # text from the h3 to get *just* the library's name
            name = self.root_locator.find_element(*self._name).text
            version = self.root_locator.find_element(*self._version).text
            return str(name).replace(version, "").rstrip()    
            
        def click_edit(self):
            self.root_locator.find_element(*self._edit_btn).click()
            
        def click_delete(self):
            self.root_locator.find_element(*self._delete_btn).click()
            
        def click_public(self):
            self.root_locator.find_element(*self._public_btn).click()
            
        def click_private(self):
            self.root_locator.find_element(*self._private_btn).click()
