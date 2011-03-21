import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page

class sign_in_to_show_dashboard(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')
    
    def testShouldSignInToShowDashboard(self):
        #This test is to check that the user should be directed to the dashboard page after signing in.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
        
        #Click on sign-in link on homepage and enter the username and password
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        
        #Check for the title of the page to confirm that we are on the dashboard page.
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #Now we need to check that when the user is logged in, he should see a My Account link on the home page and clicking on that link should take him to the dashboard.
        dashboardpage_obj.navigate_to_homepage()
        homepage_obj.click_myaccount()
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
