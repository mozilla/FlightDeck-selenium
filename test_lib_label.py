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
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
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
import home_page, login_page, dashboard_page, lib_editor_page
from unittestzero import Assert


class TestLibLabel():


    def testShouldCheckLibraryLabel(self, testsetup):
        #This test is to check the labels of a library on the dashboard
        #Create page objects
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        libpage_obj = lib_editor_page.LibraryEditorPage(testsetup)
        credentials = loginpage_obj.credentials_of_user('default')

         
        #Create a library. Then go to dashoard and assert that the label is 'initial'. 
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        loginpage_obj.login(credentials['email'], credentials['password'])
        lib_name = libpage_obj.get_lib_name()
        text_lib = lib_name
        homepage_obj.click_myaccount()
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        label_name = dashboardpage_obj.get_lib_label_name()
        Assert.true("amotesting" in label_name.text)
        
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



