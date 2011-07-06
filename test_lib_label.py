#!/usr/bin/env python

import home_page, login_page, dashboard_page, lib_editor_page
from unittestzero import Assert

#My Account Page
class TestLibLabel():


    def testShouldCheckLibraryLabel(self, testsetup):
        #This test is to check the labels of a library on the dashboard
        #Create page objects
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        libpage_obj = lib_editor_page.LibraryEditorPage(testsetup)
        username = ""
        password = ""
        
        #Create a library. Then go to dashoard and assert that the label is 'initial'. 
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        loginpage_obj.login(username, password)
        lib_name = libpage_obj.get_lib_name()
        text_lib = lib_name
        homepage_obj.click_myaccount()
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        label_name = dashboardpage_obj.get_lib_label_name()
        Assert.true("initial" in label_name.text)
        
        #Click on the edit button of the library.Then create a copy of that library and assert that the label is 'copy'
        dashboardpage_obj.navigate_to_lib_editor()
        libpage_obj.click_copy_btn()
        copy_lib_name = libpage_obj.get_lib_name()
        text_copy_lib = copy_lib_name
        try:
            Assert.not_equal(text_lib, text_copy_lib)
        except:
            print 'A copy of the addon could not be created'
        homepage_obj.click_myaccount()
        label_name = dashboardpage_obj.get_lib_label_name()
        Assert.true("copy" in label_name.text)



