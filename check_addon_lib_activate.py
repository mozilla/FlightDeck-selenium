#!/usr/bin/env python

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page, dashboard_private_page

#My Account Page

class check_addon_activate_deactivate(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.connect('firefox')

    def testShouldCheckAddonDeactivateAndActivate(self):
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        privatepage_obj = dashboard_private_page.DashboardPrivatePage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
    
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        #Get the name of the addon present at the top of the list on dashboard.
        #This will be used to compare whether the addon is removed from the top of list after making it private
        addon_name = dashboardpage_obj.get_top_addon_name()
        
        #Click on the private button to make it private and then check that the addon is not in the list anymore
        dashboardpage_obj.click_addon_mkprivate_btn()
        new_top_addon_name = dashboardpage_obj.get_top_addon_name()
        self.assertNotEqual(addon_name, new_top_addon_name)
        dashboardpage_obj.go_to_private_addons_page()

        #Go to the private addons page and check that the addon that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the addon is present there.
        priv_addon_name = privatepage_obj.get_top_addon_name()
        #text_priv_addon = priv_addon_name.text
        #print text_priv_addon
        self.assertEquals(addon_name, priv_addon_name)
        privatepage_obj.click_addon_mkpublic_btn()
        new_priv_top_addon_name = privatepage_obj.get_top_addon_name()
        self.assertNotEqual(priv_addon_name, new_priv_top_addon_name)
        privatepage_obj.go_to_dashboard()
        top_addon = dashboardpage_obj.get_top_addon_name()
        self.assertEquals(priv_addon_name, top_addon)
        

    def testShouldCheckLibDeactivateAndActivate(self):
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        privatepage_obj = dashboard_private_page.DashboardPrivatePage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
        
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #Get the name of the library present at the top of the library list on dashboard.
        #This will be used to compare whether the library is removed from the top of list after making it private
        lib_name = dashboardpage_obj.get_top_lib_name()
        
        #Click on the private button to make it private and then check that the library is not in the list anymore
        dashboardpage_obj.click_lib_mkprivate_btn()
        new_top_lib_name = dashboardpage_obj.get_top_lib_name()
        self.assertNotEqual(lib_name, new_top_lib_name)
        dashboardpage_obj.go_to_private_libs_page()

        #Go to the private libraries page and check that the library that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the library is present there.
        priv_lib_name = privatepage_obj.get_top_lib_name()
        #text_priv_addon = priv_addon_name.text
        #print text_priv_addon
        self.assertEquals(lib_name, priv_lib_name)
        privatepage_obj.click_lib_mkpublic_btn()
        new_priv_top_lib_name = privatepage_obj.get_top_lib_name()
        self.assertNotEqual(priv_lib_name, new_priv_top_lib_name)
        privatepage_obj.go_to_dashboard()
        top_lib = dashboardpage_obj.get_top_lib_name()
        self.assertEquals(priv_lib_name, top_lib)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
