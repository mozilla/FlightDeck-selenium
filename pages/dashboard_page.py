#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base_page import FlightDeckBasePage
from page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class DashboardPage(FlightDeckBasePage):

    _page_title = "Dashboard - Add-on Builder"

    _public_addons_link = (By.LINK_TEXT, "Public Add-ons")
    _public_libraries_link = (By.LINK_TEXT, "Public Libraries")
    _private_addons_link = (By.LINK_TEXT, "Private Add-ons")
    _private_libraries_link = (By.LINK_TEXT, "Private Libraries")
    _addons_public_counter = (By.ID, "public_addons_no")
    _logged_in_username_locator = (By.CSS_SELECTOR, "li.name")

    def addon(self, lookup):
        return self.Addon(self.testsetup, lookup)

    def library(self, lookup):
        return self.Library(self.testsetup, lookup)

    @property
    def logged_in_username(self):
        return self.selenium.find_element(*self._logged_in_username_locator).text

    @property
    def addons_count_label(self):
        return self.selenium.find_element(*self._addons_public_counter).text

    def addons_element_count(self):
        return len(self.selenium.find_elements(*self.Addon._base_locator))

    def click_private_addons_link(self):
        self.selenium.find_element(*self._private_addons_link).click()

    def click_private_libraries_link(self):
        self.selenium.find_element(*self._private_libraries_link).click()

    def click_public_libraries_link(self):
        self.selenium.find_element(*self._public_libraries_link).click()

    class DashboardContentRegion(Page):
        _name_locator = (By.CSS_SELECTOR, "h3")
        _version_locator = (By.CSS_SELECTOR, "h3 > span.version")
        _edit_locator = (By.CSS_SELECTOR, "li.UI_Edit_Version > a")
        _delete_locator = (By.CSS_SELECTOR, "li.UI_Delete > a")
        _public_locator = (By.CSS_SELECTOR, "li.UI_Activate > a")
        _private_locator = (By.CSS_SELECTOR, "li.UI_Disable > a")
        _confirm_delete_locator = (By.ID, 'delete_package')

        def __init__(self, testsetup, lookup):
            Page.__init__(self, testsetup)
            if type(lookup) is int:
                self._root_locator = (self._base_locator[0], "%s[%i]" % (self._base_locator[1], lookup))
            elif type(lookup) is unicode:
                self._root_locator = (self._base_locator[0], "%s[h3[normalize-space(text()) = '%s']]" % (self._base_locator[1], lookup))

        @property
        def _root_element(self):
            return self.selenium.find_element(*self._root_locator)

        @property
        def is_displayed(self):
            return self.is_element_visible(*self._root_locator)

        def click_edit(self):
            self._root_element.find_element(*self._edit_locator).click()

            if 'Add-ons' in self._base_locator[1]:
                from pages.editor_page import AddonEditorPage
                return  AddonEditorPage(self.testsetup)
            elif 'Libraries' in self._base_locator[1]:
                from pages.editor_page import LibraryEditorPage
                return LibraryEditorPage(self.testsetup)

        def click_delete(self):
            self._root_element.find_element(*self._delete_locator).click()

        def confirm_delete(self):
            self.selenium.find_element(*self._confirm_delete_locator).click()
            WebDriverWait(self.selenium, 10).until(lambda s: not self.is_element_present(*self._root_locator),
                'Package element did not disappear from the DOM before the timout')

        def click_public(self):
            self._root_element.find_element(*self._public_locator).click()
            WebDriverWait(self.selenium, 10).until(lambda s: not self.is_element_present(*self._root_locator),
                'Package element did not disappear from the DOM before the timout')

        def click_private(self):
            self._root_element.find_element(*self._private_locator).click()
            WebDriverWait(self.selenium, 10).until(lambda s: not self.is_element_present(*self._root_locator),
                'Package element did not disappear from the DOM before the timout')

        @property
        def name(self):
            # here we are stripping the <span class="version">
            # text from the h3 to get *just* the addon's name
            name = self._root_element.find_element(*self._name_locator).text
            version = self._root_element.find_element(*self._version_locator).text
            return name.replace(version, "").rstrip()

    class Addon(DashboardContentRegion):
        _base_locator = (By.XPATH, "//section[@id='app-content']/ul[preceding-sibling::h2[contains(text(),'Add-ons')]][1]/li")
        _test_locator = (By.CSS_SELECTOR, "li.UI_Try_in_Browser > a")

        def click_test(self):
            self.root_element.find_element(self._test_locator).click()

    class Library(DashboardContentRegion):
        _base_locator = (By.XPATH, "//section[@id='app-content']/ul[preceding-sibling::h2[contains(text(),'Libraries')]][1]/li")
