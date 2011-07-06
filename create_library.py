import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page

class create_library(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')
    
    def testShouldCreateLibrary(self):
        #This test is to check that we should be able to create a library.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        libpage_obj = lib_editor_page.LibraryEditorPage(sel)
        username = "amo.test.acc@gmail.com"
        password = "qwertyasdf"
        
        #Click on creatae library button on homepage, login and check that the library name for the current library starts with "My Library"
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        loginpage_obj.login(username, password)
        lib_name = libpage_obj.get_lib_name()
        #self.assertEquals(addon_name.text, "regexp:"+account_name.text+".*")
        self.failUnless(re.match("My Library", lib_name))

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
