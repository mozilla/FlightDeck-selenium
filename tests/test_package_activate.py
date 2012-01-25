#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.addon_editor_page import AddonEditorPage
from pages.library_editor_page import LibraryEditorPage
from unittestzero import Assert


class TestPackageActivateDeactivate:

    def test_addon_activate_deactivate(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboardpage_obj = DashboardPage(mozwebqa)
        addonpage_obj = AddonEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login()
        Assert.true(dashboardpage_obj.is_the_current_page)

        # Go back to homepage and create a new addon to work with.
        dashboardpage_obj.header.click_home_logo()
        homepage_obj.click_create_addon_btn()
        addon_name = addonpage_obj.addon_name
        addonpage_obj.header.click_dashboard()

        #Click on the private button to make it private and then check that the addon is not in the list anymore
        dashboardpage_obj.addon(addon_name).click_private()
        Assert.false(dashboardpage_obj.addon(addon_name).is_displayed, "Addon %s found" % addon_name)

        #Go to the private addons page and check that the addon that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the addon is present there.
        dashboardpage_obj.click_private_addons_link()
        Assert.true(dashboardpage_obj.addon(addon_name).is_displayed, "Addon %s not found" % addon_name)

        # Switch it back to public now, addon should disappear
        dashboardpage_obj.addon(addon_name).click_public()
        Assert.false(dashboardpage_obj.addon(addon_name).is_displayed, "Addon %s found" % addon_name)

        # Should be on main dashboard page
        dashboardpage_obj.header.click_dashboard()
        Assert.true(dashboardpage_obj.addon(addon_name).is_displayed, "Addon %s not found" % addon_name)

        dashboardpage_obj.delete_test_data()

    def test_library_activate_deactivate(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboardpage_obj = DashboardPage(mozwebqa)
        librarypage_obj = LibraryEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login()
        Assert.true(dashboardpage_obj.is_the_current_page)

        # go back to homepage, create a new library to work with
        dashboardpage_obj.header.click_home_logo()
        homepage_obj.click_create_lib_btn()
        library_name = librarypage_obj.library_name
        librarypage_obj.header.click_dashboard()

        #Click on the private button to make it private and then check that the library is not in the list anymore
        dashboardpage_obj.library(library_name).click_private()
        Assert.false(dashboardpage_obj.library(library_name).is_displayed, "Library %s found" % library_name)

        #Go to the private libraries page and check that the library that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the library is present there.
        dashboardpage_obj.click_private_libraries_link()
        Assert.true(dashboardpage_obj.library(library_name).is_displayed, "Library %s not found" % library_name)

        # Switch it back to public - it should disappaer
        dashboardpage_obj.library(library_name).click_public()
        Assert.false(dashboardpage_obj.library(library_name).is_displayed, "Library %s found" % library_name)

        # Go to main dashboard, should be present
        dashboardpage_obj.header.click_dashboard()
        Assert.true(dashboardpage_obj.library(library_name).is_displayed, "Library %s not found" % library_name)

        dashboardpage_obj.delete_test_data()
