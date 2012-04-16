#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base_page import FlightDeckBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(FlightDeckBasePage):

    _create_addon_btn = (By.CSS_SELECTOR, "div.right_column div.fd_button > a")
    _create_lib_btn = (By.CSS_SELECTOR, "div.UI_Bottom_Info a[title='Create Library']")
    _browse_addons_list = (By.XPATH, "//ul[preceding-sibling::h2[text()='Browse Add-ons']]/li[@class='UI_Item']")
    _browse_libraries_list = (By.XPATH, "//ul[preceding-sibling::h2[text()='Browse Libraries']]/li[@class='UI_Item']")

    @property
    def browse_addons_count(self):
        return len(self.selenium.find_elements(*self._browse_addons_list))

    @property
    def browse_libraries_count(self):
        return len(self.selenium.find_elements(*self._browse_libraries_list))

    def click_create_addon_btn(self):
        self.selenium.find_element(*self._create_addon_btn).click()
        from pages.editor_page import AddonEditorPage
        addon_editor = AddonEditorPage(self.testsetup)
        WebDriverWait(self.selenium, 10).until(lambda s: addon_editor.tab(0).selected)
        self.add_id()
        return addon_editor

    def click_create_lib_btn(self):
        self.selenium.find_element(*self._create_lib_btn).click()
        from pages.editor_page import LibraryEditorPage
        library_editor = LibraryEditorPage(self.testsetup)
        WebDriverWait(self.selenium, 10).until(lambda s: library_editor.tab(0).selected)
        self.add_id()
        return library_editor
