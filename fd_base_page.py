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
from page import Page
from selenium.webdriver.common.by import By


class FlightDeckBasePage(Page):
    
    def go_to_home_page(self):
        self.selenium.get(self.base_url)
       
    @property
    def header(self):
        return FlightDeckBasePage.HeaderRegion(self.testsetup)
       
    class HeaderRegion(Page):
       
        _home_link_locator = (By.CSS_SELECTOR, "#flightdeck-logo > a")
        _search_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(2) > span > a")
        _documentation_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(3) > span > a")
        _signin_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(4) > span > a")
        _myaccount_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(4) a[title='My Account']")
        _signout_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(4) a[title='Sign Out']")
       
        def click_home_logo(self):
            self.selenium.find_element(*self._home_link_locator).click()
       
        def click_search(self):
            self.selenium.find_element(*self._search_link_locator).click()
           
        def click_documentation(self):
            self.selenium.find_element(*self._documentation_link_locator).click()
               
        def click_signin(self):
            self.selenium.find_element(*self._signin_link_locator).click()
           
        def click_dashboard(self):
            self.selenium.find_element(*self._myaccount_link_locator).click()
       
        def click_signout(self):
            self.selenium.find_element(*self._signout_link_locator).click()
       
            