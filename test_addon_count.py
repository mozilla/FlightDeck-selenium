#!/usr/bin/env python

import string
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page
from unittestzero import Assert

#My Account Page
class TestLibLabelcheck_lib_label():

    def testAddonCount(self, testsetup):
        #This test is to assert that the count of the addons on dashboard is equal to the number of addons present on the page.
        #Create page objects
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        username = '' 
        password = ''

        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())

        #Get the total count of the number of add-ons that are displayed on the dashboard.
        addon_count = dashboardpage_obj.calc_total_addons()

        #Get the number of addons that are displayed on the left hand side of the page.(Something like your add-ons(20))
        counter = dashboardpage_obj.get_addons_count()
        counter = string.lstrip(counter, '(')
        counter = string.rstrip(counter, ')')

        #Assert that the total addons on the page matches the counter on the left hand side.
        Assert.equal(str(addon_count), str(counter))

