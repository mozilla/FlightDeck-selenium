import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, addon_editor_page

class create_add_on(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')
    
    def testShouldCreateAddOn(self):
        #This test is to check that we should be able to create an addon.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        addonpage_obj = addon_editor_page.AddonEditorPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
        
        #Click on sign-in link on homepage, enter the username and password, and assert that you are on the dashboard page
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #Get the account name displayed on the dashboard
        account_name = dashboardpage_obj.get_account_name()
        text_acc = account_name.text
        homepage_obj.go_to_home_page()

        #Click on create addon button on homepage and compare the addon name should be same as account name
        homepage_obj.click_create_addon_btn()
        addon_name = addonpage_obj.get_addon_name()
        text_addon = addon_name.text
        #print text_addon
        self.failUnless(re.match(text_acc, text_addon))
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
