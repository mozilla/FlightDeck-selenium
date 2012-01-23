#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from page import Page
from selenium.webdriver.common.by import By


class EditorTabRegion(Page):

    _tab_selector = (By.CSS_SELECTOR, 'div.tab-container span.tab')
    _textarea = (By.CSS_SELECTOR, 'div.ace_text-layer')

    def __init__(self, testsetup, lookup):
        Page.__init__(self, testsetup)
        self.lookup = lookup - 1
        self._root_element = self.selenium.find_elements(*self._tab_selector)[self.lookup]

    @property
    def content(self):
        return self.selenium.find_element(*self._textarea).text

    @property
    def selected(self):
        return 'selected' in self._root_element.get_attribute('class')
