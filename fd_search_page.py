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
# Contributor(s): Zac Campbell
#                 
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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchPage(FlightDeckBasePage):
    
    _search_field_locator = (By.CSS_SELECTOR, "#Search > input[type='search']")
    _search_btn = (By.CSS_SELECTOR, "#Search > button[type='submit']")
    
    def type_and_click_search(self, text):
        self.selenium.find_element(*self._search_field_locator).sendkeys(text)
        
    @property
    def addon(index):
        return self.AddonRegion(self.testsetup, index)
        
    @property
    def library(index):
        return self.LibraryRegion(self.testsetup, index)
        
        
    class AddonRegion(FlightDeckBasePage):
    
        def __init__(self, testsetup, index):
            FlightDeckBasePage.__init__(self, testsetup)
            self.index = index
           
        _addon = (By.XPATH, "//div[preceding-sibling::h2[contains(text(),'Add-on Results')]]" +
                  "[not(preceding-sibling::h2[contains(text(),'Library Results')])]")
    
        _name = (By.CSS_SELECTOR, "h3:not(span)")
        _test_btn = (By.CSS_SELECTOR, "li.UI_Try_in_Browser > a")  
        _source_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a")
        
        @property
        def root_locator(self):
            return self.selenium.find_elements(*self._addon)[self.index-1]
    
        @property
        def name(self):
            return self.root_locator.find_element(*self._name).text

        def click_source(self):
            self.root_locator.find_element(*self._edit_btn).click()

        def click_test(self):
            self.root_locator.find_element(*self._test_btn).click()


    class LibraryRegion(FlightDeckBasePage):
    
        def __init__(self, testsetup, index):
            FlightDeckBasePage.__init__(self, testsetup)
            self.index = index
           
        _lib = (By.XPATH, "//div[preceding-sibling::h2[contains(text(),'Library Results')]]")
    
        _name = (By.CSS_SELECTOR, "h3:not(span)")
        _source_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a")
        
        @property
        def root_locator(self):
            return self.selenium.find_elements(*self._addon)[self.index-1]
    
        @property
        def name(self):
            return self.root_locator.find_element(*self._name).text

        def click_source(self):
            self.root_locator.find_element(*self._edit_btn).click()