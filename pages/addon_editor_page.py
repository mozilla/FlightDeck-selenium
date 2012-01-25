#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from pages.base_page import FlightDeckBasePage
from pages.regions.editor_tab_region import EditorTabRegion
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class AddonEditorPage(FlightDeckBasePage):

    _addon_name = (By.ID, 'package-info-name')
    _copy_locator = (By.ID, 'package-copy')
    _save_locator = (By.ID, 'package-save')
    _save_spinner_locator = (By.CSS_SELECTOR, '#package-save.loading')
    _properties_locator = (By.ID, 'package-properties')
    _version_locator = (By.ID, 'version_name')
    _addon_name_input_locator = (By.ID, 'full_name')
    _properties_save_locator = (By.ID, 'savenow')

    @property
    def addon_name(self):
        return self.selenium.find_element(*self._addon_name).text

    def click_copy(self):
        self.selenium.find_element(*self._copy_locator).click()
        self.add_id()

    def click_save(self):
        self.selenium.find_element(*self._save_locator).click()
        self._wait_for_save()

    def click_properties(self):
        self.selenium.find_element(*self._properties_locator).click()

    def type_addon_name(self, value):
        self.selenium.find_element(*self._addon_name_input_locator).clear()
        self.selenium.find_element(*self._addon_name_input_locator).send_keys(value)

    def click_properties_save(self):
        self.selenium.find_element(*self._properties_save_locator).click()
        self._wait_for_save()

    def type_addon_version(self, version_label):
        save_button = self.selenium.find_element(*self._save_locator)
        ActionChains(self.selenium).move_to_element(save_button).perform()
        version_field = self.selenium.find_element(*self._version_locator)
        version_field.clear()
        version_field.send_keys(version_label)

    def tab(self, lookup):
        return EditorTabRegion(self.testsetup, lookup)

    def _wait_for_save(self):
        WebDriverWait(self.selenium, 10).until(lambda s: not self.is_element_present(*self._save_spinner_locator))
