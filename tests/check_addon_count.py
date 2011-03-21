#!/usr/bin/env python

import unittest, time, re, string
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page
from run import settings

#My Account Page
class check_lib_label(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')

    def testAddonCount(self):
        #This test is to assert that the count of the addons on dashboard is equal to the number of addons present on the page.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        username = settings.AMO_USERNAME
        password = settings.AMO_PASSWORD

        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())

        #Get the total count of the number of add-ons that are displayed on the dashboard.
        addon_count = dashboardpage_obj.calc_total_addons()

        #Get the number of addons that are displayed on the left hand side of the page.(Something like your add-ons(20))
        counter = dashboardpage_obj.get_addons_count()
        counter = string.lstrip(counter, '(')
        counter = string.rstrip(counter, ')')

        #Assert that the total addons on the page matches the counter on the left hand side.
        self.assertEquals(str(addon_count), str(counter))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
