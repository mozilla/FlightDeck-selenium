#!/usr/bin/env python

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page

#My Account Page

class check_buttons_present(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.connect('firefox')

    def testShouldCheckAddonButtonsPresent(self):
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
    
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #On the dashboard, check that the addon has "Test", "Edit", Delete", "Public" and "Private" button present
        self.assertTrue(dashboardpage_obj.check_addon_test_btn_present())
        self.assertTrue(dashboardpage_obj.check_addon_edit_btn_present())
        self.assertTrue(dashboardpage_obj.check_addon_delete_btn_present())
        self.assertTrue(dashboardpage_obj.check_addon_public_btn_present())
        self.assertTrue(dashboardpage_obj.check_addon_private_btn_present())
        
    def testShouldCheckLibButtonsPresent(self):
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
        
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())

        #On the dashboard, check that the library has ""Edit", Delete", "Public" and "Private" button present
        self.assertTrue(dashboardpage_obj.check_lib_edit_btn_present())
        self.assertTrue(dashboardpage_obj.check_lib_delete_btn_present())
        self.assertTrue(dashboardpage_obj.check_lib_public_btn_present())
        self.assertTrue(dashboardpage_obj.check_lib_private_btn_present())
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
