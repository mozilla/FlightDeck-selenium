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
import fd_home_page, fd_login_page, fd_dashboard_page, fd_addon_editor_page, fd_lib_editor_page
from unittestzero import Assert


class TestAddonLibDelete():

    def testShouldCheckAddonDelete(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(testsetup)
        addonpage_obj = fd_addon_editor_page.AddonEditorPage(testsetup)
        
        credentials = loginpage_obj.credentials_of_user('default')


        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        loginpage_obj.login(credentials['email'], credentials['password'])
        #Get the name of the addon on the editor page.
        addon_name = addonpage_obj.addon_name

        #Go the the dashboard and delete the addon that you just created. Then check that the addon at the top of the list is not the same as the one you just deleted.
        homepage_obj.header.click_dashboard()
        top_addon_name = dashboardpage_obj.addon(1).name
        dashboardpage_obj.addon(1).click_delete()
        dashboardpage_obj.confirm_delete()
        top_addon_name_after_delete = dashboardpage_obj.addon(1).name
        Assert.not_equal(top_addon_name, top_addon_name_after_delete)
        
        #Go to homepage and create a new addon and check that its name is the same as the one that was just deleted.
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        new_addon_name = addonpage_obj.addon_name

        Assert.equal(new_addon_name, addon_name)

    def testShouldCheckLibDelete(self, testsetup):

        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(testsetup)
        libpage_obj = fd_lib_editor_page.LibraryEditorPage(testsetup)
        
        credentials = loginpage_obj.credentials_of_user('default')
        
        homepage_obj.go_to_home_page()

        homepage_obj.click_create_lib_btn()
        loginpage_obj.login(credentials['email'], credentials['password'])
        lib_name = libpage_obj.lib_name

        homepage_obj.header.click_dashboard()
        top_lib_name = dashboardpage_obj.library(1).name

        dashboardpage_obj.library(1).click_delete()
        dashboardpage_obj.confirm_delete()
        top_lib_name_after_delete = dashboardpage_obj.library(1).name
        Assert.not_equal(top_lib_name, top_lib_name_after_delete)
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        
        new_lib_name = libpage_obj.lib_name
        Assert.equal(new_lib_name, lib_name)
