#!/usr/bin/env python

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page

#My Account Page
class check_lib_label(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')

    def testShouldCheckLibraryLabel(self):
        #This test is to check the labels of a library on the dashboard
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        libpage_obj = lib_editor_page.LibraryEditorPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
        
        #Create a library. Then go to dashoard and assert that the label is 'initial'. 
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        loginpage_obj.login(username, password)
        lib_name = libpage_obj.get_lib_name()
        text_lib = lib_name.text
        homepage_obj.click_myaccount()
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        label_name = dashboardpage_obj.get_lib_label_name()
        self.assertEqual("initial", label_name.text)
        
        #Click on the edit button of the library.Then create a copy of that library and assert that the label is 'copy'
        dashboardpage_obj.navigate_to_lib_editor()
        libpage_obj.click_copy_btn()
        copy_lib_name = libpage_obj.get_lib_name()
        text_copy_lib = copy_lib_name.text
        try:
            self.assertNotEqual(text_lib, text_copy_lib)
        except:
            print 'A copy of the addon could not be created'
        homepage_obj.click_myaccount()
        label_name = dashboardpage_obj.get_lib_label_name()
        self.assertEqual("copy", label_name.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

