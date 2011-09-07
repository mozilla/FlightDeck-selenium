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
from unittestzero import Assert


class TestLibLabelcheck_lib_label():

    def testAddonCount(self, mozwebqa):
        #This test is to assert that the count of the addons on dashboard is equal to the number of addons present on the page.
        #Create page objects
        homepage_obj = fd_home_page.HomePage(mozwebqa)
        loginpage_obj = fd_login_page.LoginPage(mozwebqa)
        dashboardpage_obj = fd_dashboard_page.DashboardPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login('default')
        Assert.true(dashboardpage_obj.is_the_current_page)

        #Get the total count of the number of add-ons that are displayed on the dashboard.
        addon_count = dashboardpage_obj.addons_element_count()

        #Get the number of addons that are displayed on the left hand side of the page.(Something like your add-ons(20))
        counter = dashboardpage_obj.addons_count_label

        #Assert that the total addons on the page matches the counter on the left hand side.
        Assert.equal(str(addon_count), str(counter))

