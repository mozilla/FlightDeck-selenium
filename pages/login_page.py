#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import FlightDeckBasePage


class LoginPage(FlightDeckBasePage):

    _page_title = "Sign In - Add-on Builder"
    _page_url = "/user/signin/"

    _browser_id_link_locator = (By.ID, 'UI_BrowserID_Img')

    def login(self, user="default"):
        if self._page_url not in self.selenium.current_url:
            self.selenium.get(self.base_url + self._page_url)

        self.selenium.find_element(*self._browser_id_link_locator).click()

        from pages.browser_id import BrowserID
        pop_up = BrowserID(self.testsetup)
        pop_up.login_browser_id(user)
        pop_up.sign_in()

        WebDriverWait(self.selenium, 10).until(lambda s: self.header.logged_in)
