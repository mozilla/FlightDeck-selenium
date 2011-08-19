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
    _public_libs_link = (By.LINK_TEXT, "Public Libraries")
    _private_addons_link = (By.LINK_TEXT, "Private Add-ons")
    _private_libs_link = (By.LINK_TEXT, "Private Libraries")
    
    _confirm_delete_btn = (By.ID, 'delete_package')
    
    _addons_list = (By.XPATH, "//section[@id='app-content']/ul[1]/li")
    _libs_list = (By.XPATH, "//section[@id='app-content']/ul[2]/li")
    
    _addons_public_counter = (By.ID, "public_addons_no")
    

    def addon(self, index):
        return self.AddonRegion(self.testsetup, index)

    def library(self, index):
        return self.LibRegion(self.testsetup, index)
        
    @property
    def addons_count(self):
        counter = self.selenium.find_element(*self._addons_public_counter).text
        return counter

    def calc_total_addons(self):
        elements = self.selenium.find_elements(*self._addons_list)
        return len(elements)
        
    def go_to_private_addons_page(self):
        self.selenium.find_element(*self._private_addons_link).click()
    
    def go_to_private_libs_page(self):
        self.selenium.find_element(*self._private_libs_link).click()
    
    def go_to_public_libs_page(self):
        self.selenium.find_element(*self._public_libs_link).click()

    def confirm_delete(self):
        self.selenium.find_element(*self._confirm_delete_btn).click()
          

    class AddonRegion(FlightDeckBasePage):
    
        def __init__(self, testsetup, index):
            FlightDeckBasePage.__init__(self, testsetup)
            self.index = index
           
        _addon = (By.XPATH, "//ul[preceding-sibling::h2[text()='Your Latest Add-ons']][1]/li")
    
        _name = (By.CSS_SELECTOR, "h3:not(span)")
        _test_btn = (By.CSS_SELECTOR, "li.UI_Try_in_Browser > a")  
        _edit_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a") 
        _delete_btn = (By.CSS_SELECTOR, "li.UI_Delete > a")
        _public_btn = (By.CSS_SELECTOR, "li.UI_Activate > a")
        _private_btn = (By.CSS_SELECTOR, "li.UI_Disable > a")
     
        @property
        def root_locator(self):
            return self.selenium.find_elements(*self._addon)[self.index-1]
    
        @property
        def name(self):
            return self.root_locator.find_element(*self._name).text

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


    class LibRegion(FlightDeckBasePage):
    
        def __init__(self, testsetup, index):
            FlightDeckBasePage.__init__(self, testsetup)
            self.index = index
           
        _addon = (By.XPATH, "//ul[preceding-sibling::h2[text()='Your Latest Libraries']][1]/li")
    
        _name = (By.CSS_SELECTOR, "h3:not(span)")
        _edit_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a") 
        _delete_btn = (By.CSS_SELECTOR, "li.UI_Delete > a")
        _public_btn = (By.CSS_SELECTOR, "li.UI_Activate > a")
        _private_btn = (By.CSS_SELECTOR, "li.UI_Disable > a")
     
        @property
        def root_locator(self):
            return self.selenium.find_elements(*self._addon)[self.index-1]
    
        @property
        def name(self):
            return self.root_locator.find_element(*self._name).text

        def click_edit(self):
            self.root_locator.find_element(*self._edit_btn).click()
            
        def click_delete(self):
            self.root_locator.find_element(*self._delete_btn).click()
            
        def click_public(self):
            self.root_locator.find_element(*self._public_btn).click()
            
        def click_private(self):
            self.root_locator.find_element(*self._private_btn).click()
