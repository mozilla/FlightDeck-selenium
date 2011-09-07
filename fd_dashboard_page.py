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


class DashboardPage(FlightDeckBasePage):

    _page_title = "Dashboard - Add-on Builder"

    _public_addons_link = (By.LINK_TEXT, "Public Add-ons")
    _public_libraries_link = (By.LINK_TEXT, "Public Libraries")
    _private_addons_link = (By.LINK_TEXT, "Private Add-ons")
    _private_libraries_link = (By.LINK_TEXT, "Private Libraries")
    _confirm_delete_locator = (By.ID, 'delete_package')
    _addons_public_counter = (By.ID, "public_addons_no")
   
    def addon(self, lookup):
        return DashboardContentRegion.Addon(self.testsetup, lookup)

    def library(self, lookup):
        return DashboardContentRegion.Library(self.testsetup, lookup)
        
    @property
    def addons_count_label(self):
        return self.selenium.find_element(*self._addons_public_counter).text

    def addons_element_count(self):
        return len(self.selenium.find_elements(*DashboardContentRegion._addons_locator))
    
    def click_private_addons_link(self):
        self.selenium.find_element(*self._private_addons_link).click()
    
    def click_private_libraries_link(self):
        self.selenium.find_element(*self._private_libraries_link).click()
    
    def click_public_libraries_link(self):
        self.selenium.find_element(*self._public_libraries_link).click()

    def confirm_delete(self):
        self.selenium.find_element(*self._confirm_delete_locator).click()

class DashboardContentRegion(Page):

    def __init__(self, testsetup):
        Page.__init__(self, testsetup)

    _addons_locator = (By.XPATH, "//ul[preceding-sibling::h2[text()='Your Latest Add-ons']][1]/li")
    _library_locator = (By.XPATH, "//ul[preceding-sibling::h2[text()='Your Latest Libraries']][1]/li")

    _name_locator = (By.CSS_SELECTOR, "h3")
    _version_locator = (By.CSS_SELECTOR, "h3 > span.version")
    _test_locator = (By.CSS_SELECTOR, "li.UI_Try_in_Browser > a")  
    _edit_locator = (By.CSS_SELECTOR, "li.UI_Edit_Version > a") 
    _delete_locator = (By.CSS_SELECTOR, "li.UI_Delete > a")
    _public_locator = (By.CSS_SELECTOR, "li.UI_Activate > a")
    _private_locator = (By.CSS_SELECTOR, "li.UI_Disable > a")

    def Addon(self):
        return Addon(testsetup, lookup)
        
    def Library(self):
        return Library(testsetup, lookup)

    class Addon(Page):
        
        def __init__(self, testsetup, lookup):
            Page.__init__(self, testsetup)
            self.lookup = lookup
            if type(self.lookup) is int:
                self.root_locator = (DashboardContentRegion._addons_locator[0], "%s[%s]" % (DashboardContentRegion._addons_locator, self.lookup))
            elif type(self.lookup) is unicode:
                self.root_locator = (DashboardContentRegion._addons_locator[0], "%s[h3[normalize-space(text()) = '%s']]" % (DashboardContentRegion._addons_locator[1], self.lookup))
        
        @property
        def root_element(self):
            return self.selenium.find_element(*self.root_locator)
    
        def is_displayed(self):
            return self.is_element_visible(self.root_locator)
    
        def click_test(self):
            self.root_element.find_element(*DashboardContentRegion._test_locator).click()
        
    class Library(Page):    

        def __init__(self, testsetup, lookup):
            Page.__init__(self, testsetup)
            self.lookup = lookup
            if type(self.lookup) is int:
                self.root_locator = (DashboardContentRegion._library_locator[0], "%s[%s]" % (DashboardContentRegion._library_locator, self.lookup))
            elif type(self.lookup) is unicode:
                self.root_locator = (DashboardContentRegion._library_locator[0], "%s[h3[normalize-space(text()) = '%s']]" % (DashboardContentRegion._library_locator[1], self.lookup))
            print self.root_locator
    
        @property
        def root_element(self):
            return self.selenium.find_element(*self.root_locator)

        def is_displayed(self):
            return self.is_element_visible(self.root_locator)
    
        @property
        def name(self):
            # here we are stripping thowse <span class="version">
            # text from the h3 to get *just* the addon's name
            name = self.root_element.find_element(*DashboardContentRegion._name_locator).text
            version = self.root_element.find_element(*DashboardContentRegion._version_locator).text
            return name.replace(version, "").rstrip()    
        
        def click_edit(self):
            self.root_element.find_element(*DashboardContentRegion._edit_locator).click()
