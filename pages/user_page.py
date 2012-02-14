#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base_page import FlightDeckBasePage
from selenium.webdriver.common.by import By


class UserPage(FlightDeckBasePage):
    # Page for viewing user's addons and libraries

    _username_locator = (By.CSS_SELECTOR, "#app-sidebar > h2")

    @property
    def author_name(self):
        return self.selenium.find_element(*self._username_locator).text
