#!/usr/bin/env python

from page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DashboardPage(Page):

    _account_name = "//div/aside[@id='app-sidebar']/h2"
    _home_page_click = 'flightdeck-logo'
    _top_public_addon_name = "//section[@id='app-content']/ul/li[1]/h3"
    _top_public_lib_name = "//section[@id='app-content']/ul[2]/li[1]/h3"
    _private_addons_link = (By.LINK_TEXT, "Private Add-ons")
    _private_libs_link = (By.LINK_TEXT, "Private Libraries")
    _public_libs_link = (By.LINK_TEXT, "Public Libraries")
    _addon_label_name = "//section[@id='app-content']/ul[1]/li[1]/h4"
    _lib_label_name = "//section[@id='app-content']/ul[1]/li[1]/h3"
    _addon_test_btn = (By.XPATH, "//a[@title='Test Add-on']")
    _addon_delete_btn = (By.XPATH, "//a[@title='Once and for all']") 
    _addon_edit_btn = (By.LINK_TEXT, "Edit") 
    _addon_public_btn = "//section[@id='app-content']/ul[1]/li[1]/ul[2]/li[1]/a"
    _addon_private_btn = "//section[@id='app-content']/ul[1]/li[1]/ul[2]/li[2]/a"
    _confirm_delete_btn = 'delete_package'
    _lib_edit_btn_locator = (By.CSS_SELECTOR, ".UI_Edit_Version > a")
    _lib_delete_btn = "//section[@id='app-content']/ul[2]/li[1]/ul[1]/li[2]/a"
    _lib_public_btn = "//section[@id='app-content']/ul[2]/li[1]/ul[2]/li[1]/a"
    _lib_private_btn_locator = (By.XPATH, "//a[@title='My preciousss!']")
    _addons_list = "//section[@id='app-content']/ul[1]/li"
    _libs_list = "//section[@id='app-content']/ul[2]/li"
    _addons_counter = "//aside[@id='app-sidebar']/ul/li[1]/strong"
    _libs_counter = "//aside[@id='app-sidebar']/ul/li[2]/strong"

    def __init__(self, testsetup):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = testsetup.selenium

    def get_page_title(self):
        return self.sel.title
    
    def get_account_name(self):
        return self.sel.find_element_by_xpath(self._account_name)
    
    def navigate_to_homepage(self):
        self.sel.find_element_by_id(self._home_page_click).click()
        self.sel.implicitly_wait(10)
    
    def get_top_addon_name(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        return self.sel.find_element_by_xpath(self._top_public_addon_name).text
    
    def get_top_lib_name(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        return self.sel.find_element_by_xpath(self._lib_label_name).text
    
    def get_addon_label_name(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        return self.sel.find_element_by_xpath(self._lib_label_name)
    
    def get_lib_label_name(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        return self.sel.find_element_by_xpath(self._lib_label_name)
    
    def get_addons_count(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        return self.sel.find_element_by_xpath(self._addons_counter).text
        
    def get_libs_count(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        return self.sel.find_element_by_xpath(self._libs_counter).text
        
    def calc_total_addons(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        elements = self.sel.find_elements_by_xpath(self._addons_list)
        return len(elements)
        
    def calc_total_libs(self):
        #self.sel.find_element_by_xpath(self._create_addon_btn).click()
        elements = self.sel.find_elements_by_xpath(self._libs_list)
        return len(elements)
    
    def go_to_private_addons_page(self):
        self.sel.find_element(*self._private_addons_link).click()
        self.sel.implicitly_wait(10)
    
    def go_to_private_libs_page(self):
        self.sel.find_element(*self._private_libs_link).click()
    
    def go_to_public_libs_page(self):
        self.sel.find_element(*self._public_libs_link).click()
    
    def navigate_to_addon_editor(self):
        self.sel.find_element(*self._lib_edit_btn_locator).click()
        self.sel.implicitly_wait(10)
    
    def navigate_to_lib_editor(self):
        self.sel.find_element(*self._lib_edit_btn_locator).click()
        self.sel.implicitly_wait(10)
        
    def check_addon_test_btn_present(self):
        try:
            self.sel.find_element(*self._addon_test_btn)
            return True
        except NoSuchElementException:
            return False

    def check_addon_edit_btn_present(self):
        try:
            self.sel.find_element(*self._addon_edit_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_addon_delete_btn_present(self):
        try:
            self.sel.find_element(*self._addon_delete_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_addon_public_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._addon_public_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_addon_private_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._addon_private_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_lib_edit_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._lib_edit_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_lib_delete_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._lib_delete_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_lib_public_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._lib_public_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_lib_private_btn_present(self):
        try:
            self.sel.find_element_by_xpath(self._lib_private_btn)
            return True
        except NoSuchElementException:
            return False
    
    def click_addon_mkprivate_btn(self):
        self.sel.find_element(*self._lib_private_btn_locator).click()
        self.sel.implicitly_wait(10)
        return
    
    def click_lib_mkprivate_btn(self):
        self.sel.find_element(*self._lib_private_btn_locator).click()
        self.sel.implicitly_wait(10)
        return

    def click_addon_delete(self):
        self.sel.find_element(*self._addon_delete_btn).click()
        self.sel.implicitly_wait(10)
        return

    def confirm_delete(self):
        self.sel.find_element_by_id(self._confirm_delete_btn).click()
        self.sel.implicitly_wait(10)
        return

    def click_lib_delete(self):
        self.sel.find_element(*self._addon_delete_btn).click()
        self.sel.implicitly_wait(10)
        return
    
