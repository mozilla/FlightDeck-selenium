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
import fd_home_page, fd_login_page, fd_dashboard_page, fd_lib_editor_page, fd_addon_editor_page
from unittestzero import Assert


class TestAddonActivateDeactivate():
    
    def testShouldCheckAddonDeactivateAndActivate(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(testsetup)

        credentials = homepage_obj.credentials_of_user('default')

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        
        loginpage_obj.login(credentials['email'], credentials['password'])
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        #Get the name of the addon present at the top of the list on dashboard.
        #This will be used to compare whether the addon is removed from the top of list after making it private
        addon_name = dashboardpage_obj.addon(1).name
        
        #Click on the private button to make it private and then check that the addon is not in the list anymore
        dashboardpage_obj.addon(1).click_private()
        new_top_addon_name = dashboardpage_obj.addon(1).name
        Assert.not_equal(addon_name, new_top_addon_name)
        dashboardpage_obj.go_to_private_addons_page()

        #Go to the private addons page and check that the addon that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the addon is present there.
        priv_addon_name = dashboardpage_obj.addon(1).name
        Assert.equal(addon_name, priv_addon_name)
        
        dashboardpage_obj.addon(1).click_public()
        new_priv_top_addon_name = dashboardpage_obj.addon(1).name
        Assert.not_equal(priv_addon_name, new_priv_top_addon_name)
        
        dashboardpage_obj.header.click_dashboard()
        top_addon = dashboardpage_obj.addon(1).name
        Assert.equal(priv_addon_name, top_addon)
        

    def testShouldCheckLibDeactivateAndActivate(self, testsetup):
        homepage_obj = fd_home_page.HomePage(testsetup)
        loginpage_obj = fd_login_page.LoginPage(testsetup)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(testsetup)

        credentials = loginpage_obj.credentials_of_user('default')

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login(credentials['email'], credentials['password'])
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #Get the name of the library present at the top of the library list on dashboard.
        #This will be used to compare whether the library is removed from the top of list after making it private
        lib_name = dashboardpage_obj.library(1).name
        
        #Click on the private button to make it private and then check that the library is not in the list anymore
        dashboardpage_obj.library(1).click_private()
        new_top_lib_name = dashboardpage_obj.library(1).name
        Assert.not_equal(lib_name, new_top_lib_name)
        dashboardpage_obj.go_to_private_libs_page()

        #Go to the private libraries page and check that the library that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the library is present there.
        priv_lib_name = dashboardpage_obj.library(1).name

        #print text_priv_addon
        Assert.equal(lib_name, priv_lib_name)
        
        dashboardpage_obj.library(1).click_public()
        new_priv_top_lib_name = dashboardpage_obj.library(1).name
        Assert.not_equal(priv_lib_name, new_priv_top_lib_name)
        
        dashboardpage_obj.header.click_dashboard()
        top_lib = dashboardpage_obj.library(1).name
        Assert.equal(priv_lib_name, top_lib)
