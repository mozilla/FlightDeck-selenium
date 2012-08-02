#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import urllib
import urllib2
import re


class FlightDeckBasePage(Page):

    _garbage = []

    def go_to_home_page(self):
        self.selenium.get(self.base_url)
        from pages.home_page import HomePage
        return HomePage(self.testsetup)

    def add_id(self):
        m = re.search("package\/([0-9]*)", self.selenium.current_url)
        id = m.group()

        if id not in self._garbage:
            self._garbage.append(id)

    def delete_test_data(self):
        # use urllib so we can do all this stuff silently without selenium

        # first loop through and delete all addon/libs added
        for i in self._garbage:
            delete_url = "%s/package/delete/%s/" % (self.base_url, i)
            try:
                print "deleting %s" % delete_url
                self.selenium.get(delete_url)
            except:
                # suppress any exceptions because we don't want the test to fail
                print "Delete package %s failed" % i

    @property
    def header(self):
        return FlightDeckBasePage.HeaderRegion(self.testsetup)

    class HeaderRegion(Page):

        _home_link_locator = (By.CSS_SELECTOR, "#flightdeck-logo > a")
        _create_locator = (By.CSS_SELECTOR, "div.UI_middleWrapper > nav > ul > li > span")
        _search_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(2) > span > a")
        _documentation_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(3) > span > a")
        _signin_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(4) > span > a")
        _myaccount_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(4) a[title='My Account']")
        _signout_link_locator = (By.CSS_SELECTOR, "header#app-header nav > ul > li:nth-child(4) a[title='Sign Out']")

        @property
        def logged_in(self):
            return self.is_element_visible(*self._signout_link_locator)

        @property
        def logged_out(self):
            return self.is_element_visible(*self._signin_link_locator)

        @property
        def documentation_link(self):
            return self.selenium.find_element(*self._documentation_link_locator).get_attribute('href')

        def click_home_logo(self):
            self.selenium.find_element(*self._home_link_locator).click()
            from pages.home_page import HomePage
            return HomePage(self.testsetup)

        def click_search(self):
            self.selenium.find_element(*self._search_link_locator).click()
            from pages.search_page import SearchPage
            return SearchPage(self.testsetup)

        def click_documentation(self):
            self.selenium.find_element(*self._documentation_link_locator).click()

        def click_signin(self):
            self.selenium.find_element(*self._signin_link_locator).click()
            from pages.login_page import LoginPage
            return LoginPage(self.testsetup)

        def click_dashboard(self):
            self.selenium.find_element(*self._myaccount_link_locator).click()
            from pages.dashboard_page import DashboardPage
            return DashboardPage(self.testsetup)

        def click_signout(self):
            self.selenium.find_element(*self._signout_link_locator).click()
            from pages.home_page import HomePage
            return HomePage(self.testsetup)

        def click_create_addon(self):
            create_link = self.selenium.find_element(*self._create_locator)
            ActionChains(self.selenium).move_to_element_with_offset(create_link, 5, 5).perform()
            self.selenium.find_element_by_link_text("Add-on").click()

        def click_create_library(self):
            create_link = self.selenium.find_element(*self._create_locator)
            ActionChains(self.selenium).move_to_element_with_offset(create_link, 5, 5).perform()
            self.selenium.find_element_by_link_text("Library").click()
