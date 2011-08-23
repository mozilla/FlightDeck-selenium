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
    
    _search_field_locator = (By.CSS_SELECTOR, "form#Search input[type='search']")
    _search_btn = (By.CSS_SELECTOR, "form#Search button[type='submit']")
    
    _filter_by_addons = (By.LINK_TEXT, "Add-ons")
    _filter_by_libraries = (By.LINK_TEXT, "Libraries")
    
    _addon_count_label = (By.XPATH, "//strong[preceding-sibling::a[contains(text(),'Add-ons')]]")
    _library_count_label = (By.XPATH, "//strong[preceding-sibling::a[contains(text(),'Libraries')]]")
    
    _results_message = (By.CSS_SELECTOR, "#SearchResults > p")
    
    # TODO repair locator when bug fixed
    # https://bugzilla.mozilla.org/show_bug.cgi?id=680422 
    _addon_list = (By.XPATH, "//div[preceding-sibling::h2[contains(text(),'Add-on Results')]]" +
        "[not(preceding-sibling::h2[contains(text(),'Library Results')])]")
    _library_list = (By.XPATH, "//div[preceding-sibling::h2[contains(text(),'Library Results')]]")
    
    def _item_locator_by_name(self, name):
        return (By.LINK_TEXT, name)
    
    def type_into_search(self, text):
        self.selenium.find_element(*self._search_field_locator).send_keys(text)
        
    def click_search(self):
        self.selenium.find_element(*self._search_btn).click()
        
    def is_addon_present(self, name):
        list = self.selenium.find_elements(*self._addon_list)
        return list.find_element(*self._item_locator_by_name(name)).is_displayed()
        
    def click_filter_addons_link(self):
        self.selenium.find_element(*self._filter_by_addons).click()
        
    def click_filter_libraries_link(self):
        self.selenium.find_element(*self._filter_by_libraries).click()
        
    def addons_element_count(self):
        return len(self.selenium.find_elements(*self._addon_list))
    
    @property
    def addons_count_label(self):
        label = self.selenium.find_element(*self._addon_count_label).text
        return int(str(label).replace("(","").replace(")",""))

    def library_element_count(self):
        return len(self.selenium.find_elements(*self._library_list))

    @property
    def library_count_label(self):
        label = self.selenium.find_element(*self._library_count_label).text
        return int(str(label).replace("(","").replace(")",""))
        
    def addon(self, index):
        return self.Addon(self.testsetup, index)
        
    def library(self, index):
        return self.Library(self.testsetup, index)
        
        
    class Addon(Page):
    
        def __init__(self, testsetup, index):
            Page.__init__(self, testsetup)
            self.index = index
           
        # TODO repair locator when bug fixed
        # https://bugzilla.mozilla.org/show_bug.cgi?id=680422 
        _addon = (By.XPATH, "//div[preceding-sibling::h2[contains(text(),'Add-on Results')]]" +
                  "[not(preceding-sibling::h2[contains(text(),'Library Results')])]")
    
        _name = (By.CSS_SELECTOR, "h3")
        _by_link = (By.CSS_SELECTOR, "h3 > span > a")
        _by_span_tag = (By.CSS_SELECTOR, "h3 > span")
        _test_btn = (By.CSS_SELECTOR, "li.UI_Try_in_Browser > a")  
        _source_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a")
        
        @property
        def root_locator(self):
            return self.selenium.find_elements(*self._addon)[self.index-1]
            
        @property
        def name(self):
            # stripping the author from the name to be left with just the name
            name = self.root_locator.find_element(*self._name).text
            by_tag = self.root_locator.find_element(*self._by_span_tag).text
            return str(name).replace(by_tag, "").rstrip()
        
        @property
        def author_name(self):
            return self.root_locator.find_element(*self._by_link).text

        def click_source(self):
            self.root_locator.find_element(*self._source_btn).click()

        def click_test(self):
            self.root_locator.find_element(*self._test_btn).click()

        def click_by_link(self):
            self.root_locator.find_element(*self._by_link).click()


    class Library(Page):
    
        def __init__(self, testsetup, index):
            Page.__init__(self, testsetup)
            self.index = index
           
        # TODO repair locator when bug fixed
        # https://bugzilla.mozilla.org/show_bug.cgi?id=680422
        _library = (By.XPATH, "//div[preceding-sibling::h2[contains(text(),'Library Results')]]")

        _name = (By.CSS_SELECTOR, "h3")
        _by_link = (By.CSS_SELECTOR, "h3 > span > a")
        _by_span_tag = (By.CSS_SELECTOR, "h3 > span")
        _source_btn = (By.CSS_SELECTOR, "li.UI_Edit_Version > a")
        
        @property
        def root_locator(self):
            return self.selenium.find_elements(*self._library)[self.index-1]
    
        @property
        def name(self):
            # stripping the author from the name to be left with just the name
            name = self.root_locator.find_element(*self._name).text
            by_tag = self.root_locator.find_element(*self._by_span_tag).text
            return str(name).replace(by_tag, "").rstrip()

        @property
        def author_name(self):
            return self.root_locator.find_element(*self._by_link).text
            
        def click_source(self):
            self.root_locator.find_element(*self._source_btn).click()
            
        def click_by_link(self):
            self.root_locator.find_element(*self._by_link).click()
