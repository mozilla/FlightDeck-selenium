#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home_page import HomePage
from pages.login_page import LoginPage
from unittestzero import Assert
import pytest


# These are login/logout tests with more detailed assertions intended for production runs
class TestLoginLogout:

    @pytest.mark.nondestructive
    def test_login(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        Assert.true(loginpage_obj.is_the_current_page)
        dashboard_obj = loginpage_obj.login()

        Assert.true(dashboard_obj.is_the_current_page)
        Assert.true(dashboard_obj.header.logged_in)
        Assert.equal(dashboard_obj.logged_in_username, mozwebqa.credentials['default']['name'])

    @pytest.mark.nondestructive
    def test_logout(self, mozwebqa):
        loginpage_obj = LoginPage(mozwebqa)

        dashboard_obj = loginpage_obj.login()
        Assert.true(dashboard_obj.header.logged_in)
        homepage_obj = dashboard_obj.header.click_signout()

        Assert.true(homepage_obj.header.logged_out)
