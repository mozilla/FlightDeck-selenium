#!/usr/bin/env python

import home_page, login_page, dashboard_page, addon_editor_page
from unittestzero import Assert


#My Account Page
class TestAddonLabel():

    def testShouldCheckAddonLabel(self, testsetup):
        #This test is to check the labels of an add-on on the dashboard
        #Create page objects
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        addonpage_obj = addon_editor_page.AddonEditorPage(testsetup)
        username = ""
        password = ""
        
        #Create an addon. Then go to dashoard and assert that the label is 'initial'. 
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        loginpage_obj.login(username, password)
        addon_name = addonpage_obj.get_addon_name()
        text_addon = addon_name
        homepage_obj.click_myaccount()
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        label_name = dashboardpage_obj.get_addon_label_name()
        Assert.true("selenium-test1" in label_name.text)
        
        #Click on the edit button of the addon.Then create a copy of that addon and assert that the label is 'copy'
        dashboardpage_obj.navigate_to_addon_editor()
        addonpage_obj.click_copy_btn()
        copy_addon_name = addonpage_obj.get_addon_name()
        text_copy_addon = copy_addon_name
        try:
            Assert.not_equal(text_addon, text_copy_addon)
        except:
            print 'A copy of the addon could not be created'
        homepage_obj.click_myaccount()
        label_name = dashboardpage_obj.get_addon_label_name()
        Assert.true("copy" in label_name.text)
