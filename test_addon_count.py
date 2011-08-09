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
import string
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page
from unittestzero import Assert


class TestLibLabelcheck_lib_label():

    def testAddonCount(self, testsetup):
        #This test is to assert that the count of the addons on dashboard is equal to the number of addons present on the page.
        #Create page objects
        homepage_obj = home_page.HomePage(testsetup)
        loginpage_obj = login_page.LoginPage(testsetup)
        dashboardpage_obj = dashboard_page.DashboardPage(testsetup)
        username = '' 
        password = ''

        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        Assert.equal("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())

        #Get the total count of the number of add-ons that are displayed on the dashboard.
        addon_count = dashboardpage_obj.calc_total_addons()

        #Get the number of addons that are displayed on the left hand side of the page.(Something like your add-ons(20))
        counter = dashboardpage_obj.get_addons_count()
        counter = string.lstrip(counter, '(')
        counter = string.rstrip(counter, ')')

        #Assert that the total addons on the page matches the counter on the left hand side.
        Assert.equal(str(addon_count), str(counter))

