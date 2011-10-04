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
import fd_home_page
import fd_login_page
import fd_dashboard_page
import fd_addon_editor_page
import fd_lib_editor_page
from unittestzero import Assert


class TestAddonLibDelete():

    def testShouldCheckAddonDelete(self, mozwebqa):
        homepage_obj = fd_home_page.HomePage(mozwebqa)
        loginpage_obj = fd_login_page.LoginPage(mozwebqa)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(mozwebqa)
        addonpage_obj = fd_addon_editor_page.AddonEditorPage(mozwebqa)

        loginpage_obj.login()

        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()

        #Get the name of the addon on the editor page.
        addon_name = addonpage_obj.addon_name

        #Go the the dashboard and delete the addon that you just created. Then check that the addon at the top of the list is not the same as the one you just deleted.
        homepage_obj.header.click_dashboard()
        dashboardpage_obj.addon(addon_name).click_delete()
        dashboardpage_obj.confirm_delete()
        Assert.false(dashboardpage_obj.addon(addon_name).is_displayed, "Addon %s found" % addon_name)

    def testShouldCheckLibDelete(self, mozwebqa):

        homepage_obj = fd_home_page.HomePage(mozwebqa)
        loginpage_obj = fd_login_page.LoginPage(mozwebqa)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(mozwebqa)
        libpage_obj = fd_lib_editor_page.LibraryEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj.login()

        homepage_obj.go_to_home_page()
        homepage_obj.click_create_lib_btn()
        library_name = libpage_obj.library_name

        homepage_obj.header.click_dashboard()
        dashboardpage_obj.library(library_name).click_delete()
        dashboardpage_obj.confirm_delete()
        Assert.false(dashboardpage_obj.library(library_name).is_displayed, "Library %s found" % library_name)
