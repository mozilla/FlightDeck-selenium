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
