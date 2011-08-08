#!/usr/bin/env python
from page import Page
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePage(Page):

    _create_addon_btn = "//div[@id='features-wrapper']/div/div[1]/div[2]/div/a/span"
    _create_lib_btn = (By.XPATH, "//a[@title='Create Library']")
    _signin_link = 'signin'
    _my_account_link = (By.XPATH, "//a[@title='My Account']")
    _addon_disable = "//div[@id='libs-and-extensions']/div[1]/ul[1]/li[1]/ul/li[3]/a"
    _library_disable = "//div[@id='libs-and-extensions']/div[2]/ul[1]/li[1]/ul/li[2]/a"
    _create_addon_link = "//header[@id='app-header']/div[2]/nav/ul/li[1]/div/ul/li[1]/a"
    _create_lib_link = (By.XPATH, "//span[text()='Create Library']")

    def __init__(self, testsetup):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.testsetup = testsetup
        self.sel = testsetup.selenium
        self._home_page_url = testsetup.base_url

    def go_to_home_page(self):
        self.sel.get(self._home_page_url)

    def click_signin(self):
        self.sel.find_element_by_id(self._signin_link).click()

    def click_myaccount(self):
        self.sel.find_element(*self._my_account_link).click()

    def click_create_addon_btn(self):
        self.sel.find_element_by_xpath(self._create_addon_btn).click()
    def click_create_lib_btn(self):
        self.sel.find_element(*self._create_lib_btn).click()

    def click_create_addon_link(self):
        self.sel.find_element_by_xpath(self._create_addon_link).click()

    def check_addon_disable_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._addon_disable)
            return True
        except NoSuchElementException:
            return False

    def check_lib_disable_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._library_disable)
            return True
        except NoSuchElementException:
            return False
