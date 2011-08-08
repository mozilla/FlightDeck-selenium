#!/usr/bin/env python

import home_page, login_page, dashboard_page, addon_editor_page, lib_editor_page
from unittestzero import Assert

class TestAddonLibDelete():

    def testShouldCheckAddonDelete(self, testsetup):
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        addonpage_obj = addon_editor_page.AddonEditorPage(testsetup)
        username = ""
        password = ""

        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        loginpage_obj.login(username, password)
        #Get the name of the addon on the editor page.
        addon_name = addonpage_obj.get_addon_name()

        #Go the the dashboard and delete the addon that you just created. Then check that the addon at the top of the list is not the same as the one you just deleted.
        homepage_obj.click_myaccount()
        top_addon_name = dashboardpage_obj.get_top_addon_name()
        dashboardpage_obj.click_addon_delete()
        dashboardpage_obj.confirm_delete()
        top_addon_name_after_delete = dashboardpage_obj.get_top_addon_name()
        Assert.not_equal(top_addon_name, top_addon_name_after_delete)
        
        #Go to homepage and create a new addon and check that its name is the same as the one that was just deleted.
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        new_addon_name = addonpage_obj.get_addon_name()
        print new_addon_name
        Assert.equal(new_addon_name, addon_name)

    def testShouldCheckLibDelete(self, testsetup):

        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        libpage_obj = lib_editor_page.LibraryEditorPage(testsetup)
        username = ""
        password = ""
        
        homepage_obj.go_to_home_page()

        homepage_obj.click_create_lib_btn()
        loginpage_obj.login(username, password)
        lib_name = libpage_obj.get_lib_name()
        print lib_name
        homepage_obj.click_myaccount()
        dashboardpage_obj.go_to_public_libs_page()
        top_lib_name = dashboardpage_obj.get_top_lib_name()
        print top_lib_name

        dashboardpage_obj.click_lib_delete()
        dashboardpage_obj.confirm_delete()
        top_lib_name_after_delete = dashboardpage_obj.get_top_lib_name()
        Assert.not_equal(top_lib_name, top_lib_name_after_delete)
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        new_lib_name = libpage_obj.get_lib_name()
        print new_lib_name
        Assert.equal(new_lib_name, lib_name)
