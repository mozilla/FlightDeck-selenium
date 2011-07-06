#!/usr/bin/env python

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, addon_editor_page, lib_editor_page

class check_addon_lib_delete(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')
    
    def testShouldCheckAddonDelete(self):

        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        addonpage_obj = addon_editor_page.AddonEditorPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"

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
        self.assertNotEquals(top_addon_name, top_addon_name_after_delete)
        
        #Go to homepage and create a new addon and check that its name is the same as the one that was just deleted.
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        new_addon_name = addonpage_obj.get_addon_name()
        print new_addon_name
        self.assertEquals(new_addon_name, addon_name)

    def testShouldCheckLibDelete(self):

        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        addonpage_obj = addon_editor_page.AddonEditorPage(sel)
        libpage_obj = lib_editor_page.LibraryEditorPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
        
        homepage_obj.go_to_home_page()

        homepage_obj.click_create_lib_btn()
        loginpage_obj.login(username, password)
        lib_name = libpage_obj.get_lib_name()
        print lib_name
        homepage_obj.click_myaccount()
        top_lib_name = dashboardpage_obj.get_top_lib_name()
        print top_lib_name
        dashboardpage_obj.click_lib_delete()
        dashboardpage_obj.confirm_delete()
        top_lib_name_after_delete = dashboardpage_obj.get_top_lib_name()
        self.assertNotEquals(top_lib_name, top_lib_name_after_delete)
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        new_lib_name = libpage_obj.get_lib_name()
        print new_lib_name
        self.assertEquals(new_lib_name, lib_name)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
