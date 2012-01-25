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


class TestPackageDelete:

    def test_addon_delete(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboardpage_obj = DashboardPage(mozwebqa)
        addonpage_obj = AddonEditorPage(mozwebqa)

        loginpage_obj.login()

        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()

        #Get the name of the addon on the editor page.
        addon_name = addonpage_obj.addon_name

        #Go the the dashboard and delete the addon that you just created. Then check that the addon at the top of the list is not the same as the one you just deleted.
        homepage_obj.header.click_dashboard()
        dashboardpage_obj.addon(addon_name).click_delete()
        dashboardpage_obj.addon(addon_name).confirm_delete()
        Assert.false(dashboardpage_obj.addon(addon_name).is_displayed, "Addon %s found" % addon_name)

    def test_library_delete(self, mozwebqa):

        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboardpage_obj = DashboardPage(mozwebqa)
        libpage_obj = LibraryEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj.login()

        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        library_name = libpage_obj.library_name

        homepage_obj.header.click_dashboard()
        dashboardpage_obj.library(library_name).click_delete()
        dashboardpage_obj.library(library_name).confirm_delete()
        Assert.false(dashboardpage_obj.library(library_name).is_displayed, "Library %s found" % library_name)
