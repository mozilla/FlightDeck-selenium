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

        credentials = self.testsetup.credentials[user]

        from browserid import BrowserID
        pop_up = BrowserID(self.testsetup.selenium, self.testsetup.timeout)
        pop_up.sign_in(credentials['email'], credentials['password'])

        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.header.logged_in,
            'Timed-out waiting for the login to complete')

        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.testsetup)
