#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import fd_home_page, fd_login_page, fd_search_page
import fd_dashboard_page, fd_addon_editor_page, fd_lib_editor_page, fd_user_page
from unittestzero import Assert


class TestSearch():

    def test_basic_search_string_addon(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboard_obj = fd_dashboard_page.DashboardPage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)

        credentials = loginpage_obj.credentials_of_user('default')
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login(credentials['email'], credentials['password'])

        searchterm = dashboard_obj.addon(1).name

        homepage_obj.header.click_search()
        searchpage_obj.type_into_search(searchterm)
        searchpage_obj.click_search()

        Assert.true(searchpage_obj.addon(searchterm).is_present(), "%s not found" % searchterm)

    def test_basic_search_string_library(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboard_obj = fd_dashboard_page.DashboardPage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)

        credentials = loginpage_obj.credentials_of_user('default')
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login(credentials['email'], credentials['password'])

        searchterm = dashboard_obj.library(1).name
        
        homepage_obj.header.click_search()
        searchpage_obj.type_into_search(searchterm)
        searchpage_obj.click_search()

        Assert.true(searchpage_obj.library(searchterm).is_present(), "%s not found" % searchterm)
        
    def test_search_partial_string(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()
        
        # get addon name, split string in half and search with it
        # results should be returned including the original addon
        
        top_addon_name = searchpage_obj.addon(1).name
        search_string = top_addon_name[0:4]
        searchpage_obj.type_into_search(search_string)
        searchpage_obj.click_search()
        
        Assert.true(searchpage_obj.addons_element_count() > 1)
        Assert.true(searchpage_obj.addon(top_addon_name).is_present(), "Addon '%s' not found" % top_addon_name)
                
    def test_search_no_string(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()
        
        # search with a zero length string should still return results
        # default display is for 5 addons/5 libraries
        # same as filtering by 'Combined'
        
        searchpage_obj.click_search()
        
        Assert.equal(searchpage_obj.addons_element_count(), 5)
        Assert.equal(searchpage_obj.library_element_count(), 5)
    
    def test_search_addon_filter(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()
        
        # search with a generic but safe string 'test'
        # filter by add-on results and check number
        
        searchpage_obj.type_into_search("test")
        searchpage_obj.click_search()
        
        searchpage_obj.click_filter_addons_link()

        # 20 items maximum per page        
        label_count = min(searchpage_obj.addons_count_label, 20)
        element_count = searchpage_obj.addons_element_count()

        Assert.equal(label_count, element_count)
        
    def test_search_library_filter(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()
        
        # search with a generic but safe string 'test'
        # filter by add-on results and check number
        
        searchpage_obj.type_into_search("test")
        searchpage_obj.click_search()
        
        searchpage_obj.click_filter_libraries_link()
        
        # 20 items maximum per page
        label_count = min(searchpage_obj.library_count_label, 20)
        element_count = searchpage_obj.library_element_count()
        
        Assert.equal(label_count, element_count)
    
    def test_search_author_link(self, testsetup):
        
        # go to addon result and click author link
        
        homepage_obj = fd_home_page.HomePage(testsetup)
        userpage_obj = fd_user_page.UserPage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        addon_name = searchpage_obj.addon(1).name
        author_name = searchpage_obj.addon(addon_name).author_name
        searchpage_obj.addon(addon_name).click_by_link()
        Assert.equal(userpage_obj.author_name, author_name)
        
    def test_search_library_author_link(self, testsetup):
        
        # go to library result and click author link
        homepage_obj = fd_home_page.HomePage(testsetup)
        userpage_obj = fd_user_page.UserPage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()
        
        library_name = searchpage_obj.library(1).name
        author_name = searchpage_obj.library(library_name).author_name
        searchpage_obj.library(library_name).click_by_link()
        Assert.equal(userpage_obj.author_name, author_name)

    def test_search_addon_source_btn(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboard_obj = fd_dashboard_page.DashboardPage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        editorpage_obj = fd_addon_editor_page.AddonEditorPage(testsetup)

        credentials = loginpage_obj.credentials_of_user('default')
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login(credentials['email'], credentials['password'])
        dashboard_obj.header.click_search()

        addon_name = searchpage_obj.addon(1).name
        searchpage_obj.addon(addon_name).click_source()
        Assert.equal(editorpage_obj.addon_name, addon_name)

    def test_search_library_source_btn(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboard_obj = fd_dashboard_page.DashboardPage(testsetup)
        searchpage_obj = fd_search_page.SearchPage(testsetup)
        editorpage_obj = fd_lib_editor_page.LibraryEditorPage(testsetup)

        credentials = loginpage_obj.credentials_of_user('default')
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login(credentials['email'], credentials['password'])
        dashboard_obj.header.click_search()
    
        library_name = searchpage_obj.library(1).name
        searchpage_obj.library(library_name).click_source()
        Assert.equal(editorpage_obj.lib_name, library_name)