#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By
from page import Page
from selenium.webdriver.support.ui import WebDriverWait


class Paginator(Page):

    _next_locator = (By.CSS_SELECTOR, 'ul.UI_Pagination > li.next > a')
    _results_loading_locator = (By.CSS_SELECTOR, '#SearchResults.loading')

    @property
    def is_next_visible(self):
        return self.is_element_visible(*self._next_locator)

    def next(self):
        self.selenium.find_element(*self._next_locator).click()
        self._wait_for_search_ajax()
        from pages.search_page import SearchPage
        return SearchPage(self.testsetup)

    def _wait_for_search_ajax(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: not self.is_element_present(*self._results_loading_locator),
            'The page load spinner did not disappear before the timeout')
