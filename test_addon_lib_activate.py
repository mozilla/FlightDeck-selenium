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
#                 Zac Campbell
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
    
    def testShouldCheckAddonDeactivateAndActivate(self, mozwebqa):
        homepage_obj = fd_home_page.HomePage(mozwebqa)
        loginpage_obj = fd_login_page.LoginPage(mozwebqa)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(mozwebqa)
        addonpage_obj = fd_addon_editor_page.AddonEditorPage(mozwebqa)

        credentials = mozwebqa.credentials['default']

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login(credentials['email'], credentials['password'])
        Assert.true(dashboardpage_obj.is_the_current_page)
        
        # Go back to homepage and create a new addon to work with.
        dashboardpage_obj.header.click_home_logo()
        homepage_obj.click_create_addon_btn()
        addon_name = addonpage_obj.addon_name
        addonpage_obj.header.click_dashboard()
        
        #Click on the private button to make it private and then check that the addon is not in the list anymore
        dashboardpage_obj.addon(addon_name).click_private()
        Assert.false(dashboardpage_obj.addon(addon_name).is_displayed(), "Addon %s found" % addon_name)
        
        #Go to the private addons page and check that the addon that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the addon is present there.
        dashboardpage_obj.click_private_addons_link()
        Assert.true(dashboardpage_obj.addon(addon_name).is_displayed(), "Addon %s not found" % addon_name)
        
        # Switch it back to public now, addon should disappear
        dashboardpage_obj.addon(addon_name).click_public()
        Assert.false(dashboardpage_obj.addon(addon_name).is_displayed(), "Addon %s found" % addon_name)
        
        # Should be on main dashboard page
        dashboardpage_obj.header.click_dashboard()
        Assert.true(dashboardpage_obj.addon(addon_name).is_displayed(), "Addon %s not found" % addon_name)
        

    def testShouldCheckLibDeactivateAndActivate(self, mozwebqa):
        homepage_obj = fd_home_page.HomePage(mozwebqa)
        loginpage_obj = fd_login_page.LoginPage(mozwebqa)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(mozwebqa)
        librarypage_obj = fd_lib_editor_page.LibraryEditorPage(mozwebqa)

        credentials = mozwebqa.credentials['default']
        
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login(credentials['email'], credentials['password'])
        Assert.true(dashboardpage_obj.is_the_current_page)
        
        # go back to homepage, create a new library to work with
        dashboardpage_obj.header.click_home_logo()
        homepage_obj.click_create_lib_btn()
        lib_name = librarypage_obj.lib_name      
        librarypage_obj.header.click_dashboard()
        
        #Click on the private button to make it private and then check that the library is not in the list anymore
        dashboardpage_obj.library(lib_name).click_private()
        Assert.false(dashboardpage_obj.library(lib_name).is_displayed(), "Library %s found" % lib_name)
        
        #Go to the private libraries page and check that the library that you just made private is present there.
        #Click on public to make it public and check on the dashboard that the library is present there.
        dashboardpage_obj.click_private_libraries_link()
        Assert.true(dashboardpage_obj.library(lib_name).is_displayed(), "Library %s not found" % lib_name)
   
        # Switch it back to public - it should disappaer             
        dashboardpage_obj.library(lib_name).click_public()
        Assert.false(dashboardpage_obj.library(lib_name).is_displayed(), "Library %s found" % lib_name)
        
        # Go to main dashboard, should be present
        dashboardpage_obj.header.click_dashboard()
        Assert.true(dashboardpage_obj.library(lib_name).is_displayed(), "Library %s not found" % lib_name)
