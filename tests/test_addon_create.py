#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home_page import HomePage
from unittestzero import Assert
from random import randint


class TestAddonCreate:

    def test_create_addon(self, mozwebqa):
        #This test is to check the labels of an add-on on the dashboard
        #Create page objects
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()

        #Create an addon. Then go to dashboard and assert that the label is 'initial'.
        homepage_obj = dashboard_obj.go_to_home_page()
        addonpage_obj = homepage_obj.click_create_addon_btn()
        addon_name = addonpage_obj.package_name

        dashboard_obj = addonpage_obj.header.click_dashboard()
        Assert.true(dashboard_obj.is_the_current_page)
        Assert.true(dashboard_obj.addon(addon_name).is_displayed, "Addon %s not found" % addon_name)

        #Click on the edit button of the addon.Then create a copy of that addon and assert that the label is 'copy'
        addonpage_obj = dashboard_obj.addon(addon_name).click_edit()
        addonpage_obj.click_copy()
        copy_addon_name = addonpage_obj.package_name

        Assert.contains(addon_name, copy_addon_name)
        Assert.contains('copy', copy_addon_name)

        dashboard_obj = homepage_obj.header.click_dashboard()
        Assert.true(dashboard_obj.addon(copy_addon_name).is_displayed, "Addon %s not found" % copy_addon_name)

        dashboard_obj.delete_test_data()

    def test_rename_addon(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()

        new_addon_name = 'renamed addon ' + str(randint(1, 1000))

        #Create an addon.
        homepage_obj = dashboard_obj.go_to_home_page()
        addonpage_obj = homepage_obj.click_create_addon_btn()

        #Click properties and change its name
        addonpage_obj.click_properties()
        addonpage_obj.type_package_name(new_addon_name)
        addonpage_obj.click_properties_save()
        Assert.equal(addonpage_obj.package_name, new_addon_name)

        addonpage_obj.delete_test_data()
