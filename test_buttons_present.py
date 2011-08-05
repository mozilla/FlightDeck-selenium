#!/usr/bin/env python

import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page

from unittestzero import Assert

#My Account Page

class TestButtonsPresent():
    

    def testShouldCheckAddonButtonsPresent(self, testsetup):
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        username = "dburns@mozilla.com"
        password = "seleniumtest1"
    
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #On the dashboard, check that the addon has "Test", "Edit", Delete", "Public" and "Private" button present
        Assert.true(dashboardpage_obj.check_addon_test_btn_present())
        Assert.true(dashboardpage_obj.check_addon_edit_btn_present())
        Assert.true(dashboardpage_obj.check_addon_delete_btn_present())
        Assert.true(dashboardpage_obj.check_addon_public_btn_present())
        Assert.true(dashboardpage_obj.check_addon_private_btn_present())
        
    def testShouldCheckLibButtonsPresent(self, testsetup):
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        username = ""
        password = ""
        
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())

        Assert.true(dashboardpage_obj.check_addon_test_btn_present())
        Assert.true(dashboardpage_obj.check_addon_edit_btn_present())
        Assert.true(dashboardpage_obj.check_addon_delete_btn_present())
        Assert.true(dashboardpage_obj.check_addon_public_btn_present())
        Assert.true(dashboardpage_obj.check_addon_private_btn_present())
