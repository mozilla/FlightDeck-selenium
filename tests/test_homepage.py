#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home_page import HomePage
from unittestzero import Assert
import pytest


class TestHomepage:

    @pytest.mark.nondestructive
    def test_doc_link_redirects(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        link = homepage_obj.header.documentation_link
        homepage_obj.selenium.get(link)

        Assert.contains("https://addons.mozilla.org/en-US/developers/docs/sdk/latest/", homepage_obj.selenium.current_url)

    @pytest.mark.nondestructive
    def test_addons_libraries_listed_on_home(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()

        #3 of each should be present
        Assert.equal(homepage_obj.browse_addons_count, 3)
        Assert.equal(homepage_obj.browse_libraries_count, 3)
