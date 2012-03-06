#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base_page import FlightDeckBasePage
from pages.regions.editor_tab_region import EditorTabRegion
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class EditorPage(FlightDeckBasePage):

    _name_locator = (By.ID, 'package-info-name')
    _copy_locator = (By.ID, 'package-copy')
    _copy_spinner_locator = (By.CSS_SELECTOR, '#package-copy a.loading')
    _save_locator = (By.ID, 'package-save')
    _save_options_locator = (By.ID, 'package-save-options')
    _save_spinner_locator = (By.CSS_SELECTOR, '#package-save.loading')
    _properties_locator = (By.ID, 'package-properties')
    _version_locator = (By.ID, 'version_name')
    _name_input_locator = (By.ID, 'full_name')
    _properties_save_locator = (By.ID, 'savenow')

    @property
    def name(self):
        return self.selenium.find_element(*self._name_locator).text

    def click_copy(self):
        self.selenium.find_element(*self._copy_locator).click()
        self._wait_for_copy()
        self.add_id()

    def click_save(self):
        self.selenium.find_element(*self._save_locator).click()
        self._wait_for_save()

    def click_properties(self):
        self.selenium.find_element(*self._properties_locator).click()

    def type_name(self, value):
        self.selenium.find_element(*self._name_input_locator).clear()
        self.selenium.find_element(*self._name_input_locator).send_keys(value)

    def click_properties_save(self):
        self.selenium.find_element(*self._properties_save_locator).click()
        self._wait_for_save()

    def type_version(self, version_label):
        save_options_button = self.selenium.find_element(*self._save_options_locator)
        save_options_button.click()
        version_field = self.selenium.find_element(*self._version_locator)
        version_field.clear()
        version_field.send_keys(version_label)

    def tab(self, lookup):
        return EditorTabRegion(self.testsetup, lookup)

    def _wait_for_save(self):
        WebDriverWait(self.selenium, 10).until(lambda s: not self.is_element_present(*self._save_spinner_locator))

    def _wait_for_copy(self):
        WebDriverWait(self.selenium, 10).until(lambda s: not self.is_element_present(*self._copy_spinner_locator))


class AddonEditorPage(EditorPage):

    @property
    def addon_name(self):
        return self.name

class LibraryEditorPage(EditorPage):

    @property
    def library_name(self):
        return self.name
