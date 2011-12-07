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
import time
from page import Page
from pages.base_page import FlightDeckBasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class SearchPage(FlightDeckBasePage):

    _search_field_locator = (By.CSS_SELECTOR, "#Search input[type='search']")
    _search_button_locator = (By.CSS_SELECTOR, "#Search button[type='submit']")

    _filter_by_addons_locator = (By.LINK_TEXT, "Add-ons")
    _filter_by_libraries_locator = (By.LINK_TEXT, "Libraries")

    _addon_count_label_locator = (By.XPATH, "//strong[preceding-sibling::a[contains(text(),'Add-ons')]]")
    _library_count_label_locator = (By.XPATH, "//strong[preceding-sibling::a[contains(text(),'Libraries')]]")

    _copies_knob_locator = (By.CSS_SELECTOR, "#CopiesFilter div.knob")
    _used_knob_locator = (By.CSS_SELECTOR, "#UsedFilter div.knob")
    _activity_knob_locator = (By.CSS_SELECTOR, "#ActivityFilter div.knob")

    _results_message_locator = (By.CSS_SELECTOR, "#SearchResults > p")

    def addon(self, lookup):
        return self.Addon(self.testsetup, lookup)

    def library(self, lookup):
        return self.Library(self.testsetup, lookup)

    def _item_locator_by_name(self, name):
        return (By.LINK_TEXT, name)

    def type_search_term(self, text):
        self.selenium.find_element(*self._search_field_locator).send_keys(text)

    def clear_search(self):
        self.selenium.find_element(*self._search_field_locator).clear()

    def click_search(self):
        self.selenium.find_element(*self._search_button_locator).click()

    def click_filter_addons_link(self):
        self.selenium.find_element(*self._filter_by_addons_locator).click()

    def click_filter_libraries_link(self):
        self.selenium.find_element(*self._filter_by_libraries_locator).click()

    def addons_element_count(self):
        return len(self.selenium.find_elements(*self.Addon._base_locator))

    def search_for_term(self, search_term):
        self.clear_search()
        self.type_search_term(search_term)
        self.click_search()

    def search_until_package_exists(self, name, package):
        timeout = time.time() + (self.testsetup.timeout / 1000)
        sleep_time = 10 - self.testsetup.default_implicit_wait
        
        while time.time() < timeout:
            self.search_for_term(name)

            if package.is_displayed:
                break
            else:
                time.sleep(sleep_time)
                self.header.click_search()

    @property
    def addons_count_label(self):
        label = self.selenium.find_element(*self._addon_count_label_locator).text
        return int(label.strip('()'))

    def library_element_count(self):
        return len(self.selenium.find_elements(*self.Library._base_locator))

    @property
    def library_count_label(self):
        label = self.selenium.find_element(*self._library_count_label_locator).text
        return int(label.strip('()'))

    def move_copies_slider(self, notches):
        # 33 is the amount of pixels to move one notch
        x_offset = 33 * notches
        copies_knob = self.selenium.find_element(*self._copies_knob_locator)
        ActionChains(self.selenium).drag_and_drop_by_offset(copies_knob, x_offset, 0).perform()

    def move_used_packages_slider(self, notches):
        # 8 is the amount of pixels to move one notch
        x_offset = 8 * notches
        used_packages_knob = self.selenium.find_element(*self._used_knob_locator)
        ActionChains(self.selenium).drag_and_drop_by_offset(used_packages_knob, x_offset, 0).perform()

    def move_activity_slider(self, notches):
        # 38 is the amount of pixels to move one notch
        x_offset = 38 * notches
        activity_knob = self.selenium.find_element(*self._activity_knob_locator)
        ActionChains(self.selenium).drag_and_drop_by_offset(activity_knob, x_offset, 0).perform()

    class SearchResultsRegion(Page):

        def __init__(self, testsetup, lookup):
            Page.__init__(self, testsetup)
            if type(lookup) is int:
                self._root_locator = (self._base_locator[0], "%s[%i]" % (self._base_locator[1], lookup))
            elif type(lookup) is unicode:
                self._root_locator = (self._base_locator[0], "%s[descendant::h3/a[text()='%s']]" % (self._base_locator[1], lookup))

        _name_locator = (By.CSS_SELECTOR, "h3 > a")
        _author_link_locator = (By.CSS_SELECTOR, "ul.search_meta li:nth-child(1) > a")

        @property
        def root_element(self):
            return self.selenium.find_element(*self._root_locator)

        @property
        def is_displayed(self):
            return self.is_element_visible(*self._root_locator)

        @property
        def name(self):
            return self.root_element.find_element(*self._name_locator).text

        @property
        def author_name(self):
            return self.root_element.find_element(*self._author_link_locator).text

        def click(self):
            self.root_element.find_element(*self._name_locator).click()

        def click_author(self):
            self.root_element.find_element(*self._author_link_locator).click()

    class Addon(SearchResultsRegion):

        _base_locator = (By.XPATH, "//div[contains(@class,'addon')]")
        _test_btn = (By.CSS_SELECTOR, "li.UI_Try_in_Browser > a")

        def click_test(self):
            self.root_element.find_element(*self._test_btn).click()

    class Library(SearchResultsRegion):

        _base_locator = (By.XPATH, "//div[contains(@class,'library')]")
