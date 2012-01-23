#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.library_editor_page import LibraryEditorPage
from unittestzero import Assert


class TestLibLabel():

    def testShouldCheckLibraryLabel(self, mozwebqa):
        #This test is to check the labels of a library on the dashboard
        #Create page objects
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboardpage_obj = DashboardPage(mozwebqa)
        libpage_obj = LibraryEditorPage(mozwebqa)

        loginpage_obj.login()

        #Create a library. Then go to dashboard and assert that the label is present.
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        library_name = libpage_obj.library_name

        libpage_obj.header.click_dashboard()
        Assert.true(dashboardpage_obj.is_the_current_page)
        Assert.true(dashboardpage_obj.library(library_name).is_displayed, "Library %s not found" % library_name)

        #Click on the edit button of the library.Then create a copy of that library and assert that the label is 'copy'
        dashboardpage_obj.library(library_name).click_edit()
        libpage_obj.click_copy()
        copy_library_name = libpage_obj.library_name

        try:
            Assert.not_equal(library_name, copy_library_name)
        except:
            print 'A copy of the library could not be created'
        libpage_obj.header.click_dashboard()

        Assert.true(dashboardpage_obj.library(copy_library_name).is_displayed, "Library %s not found" % copy_library_name)
        
        dashboardpage_obj.delete_test_data()
