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
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Zac Campbell
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
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.dashboard_page import DashboardPage
from pages.addon_editor_page import AddonEditorPage
from pages.library_editor_page import LibraryEditorPage
from pages.user_page import UserPage
from unittestzero import Assert
import pytest
xfail = pytest.mark.xfail


class TestSearch():

    @xfail(reason = 'Webdriver cannot trigger :hover, steps to setup addon can\'t be completed')
    def test_search_by_addon_name_returns_addon(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboard_obj = DashboardPage(mozwebqa)
        addonpage_obj = AddonEditorPage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login()

        #create a new addon with the valid criteria (version not initial)
        dashboard_obj.header.click_home_logo()
        homepage_obj.click_create_addon_btn()
        addonpage_obj.type_addon_version('searchable')
        addonpage_obj.click_save()
        searchterm = addonpage_obj.addon_name

        homepage_obj.header.click_search()
        searchpage_obj.type_search_term(searchterm)
        searchpage_obj.click_search()

        Assert.true(searchpage_obj.addon(searchterm).is_displayed(), '%s not found' % searchterm)

        searchpage_obj.delete_test_data()

    @xfail(reason = 'Webdriver cannot trigger :hover, steps to setup addon can\'t be completed')
    def test_search_by_library_name_returns_library(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboard_obj = DashboardPage(mozwebqa)
        librarypage_obj = LibraryEditorPage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login()

        #create a new library with the valid criteria (version not initial)
        dashboard_obj.header.click_home_logo()
        homepage_obj.click_create_lib_btn()
        librarypage_obj.type_library_version('searchable')
        librarypage_obj.click_save()
        searchterm = librarypage_obj.lib_name

        homepage_obj.header.click_search()
        searchpage_obj.type_search_term(searchterm)
        searchpage_obj.click_search()

        Assert.true(searchpage_obj.library(searchterm).is_displayed(), '%s not found' % searchterm)

        searchpage_obj.delete_test_data()

    @xfail(reason = 'Bug 681747 - Partial strings not matching against names in FD Search')
    def test_search_partial_addon_name_returns_addon(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        # get addon name, split string in half and search with it
        # results should be returned including the original addon

        top_addon_name = searchpage_obj.addon(1).name
        search_string = top_addon_name[:4]
        searchpage_obj.type_search_term(search_string)
        searchpage_obj.click_search()

        Assert.true(searchpage_obj.addons_element_count() >= 1)
        Assert.true(searchpage_obj.addon(top_addon_name).is_displayed(), 'Addon \'%s\' not found' % top_addon_name)

    @xfail(reason = 'Bug 681747 - Partial strings not matching against names in FD Search')
    def test_search_partial_library_name_returns_library(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        # get library name, split string in half and search with it
        # results should be returned including the original addon

        top_library_name = searchpage_obj.library(1).name
        search_string = top_library_name[:4]
        searchpage_obj.type_search_term(search_string)
        searchpage_obj.click_search()

        Assert.true(searchpage_obj.library_element_count() >= 1)
        Assert.true(searchpage_obj.addon(top_library_name).is_displayed(), 'Library \'%s\' not found' % top_library_name)

    @xfail(reason = "Bug 695283 - Search not indexing add-ons")
    def test_empty_search_returns_all_results(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        # search with a zero length string should still return results
        # default display is for 5 addons/5 libraries
        # same as filtering by 'Combined'

        searchpage_obj.clear_search()
        searchpage_obj.click_search()

        Assert.equal(searchpage_obj.addons_element_count(), 5)
        Assert.equal(searchpage_obj.library_element_count(), 5)

    def test_search_addon_filter_results_match(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        # search with a generic but safe string 'test'
        # filter by add-on results and check number

        searchpage_obj.type_search_term('test')
        searchpage_obj.click_search()

        searchpage_obj.click_filter_addons_link()

        # 20 items maximum per page
        label_count = min(searchpage_obj.addons_count_label, 20)
        element_count = searchpage_obj.addons_element_count()

        Assert.equal(label_count, element_count, 'Number of items displayed should match 20 or total number of results, whichever is smallest. This is due to pagination.')

    @xfail(reason = 'Bug 689508 - label and search results mismatch')
    def test_search_library_filter_results_match(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        # search with a generic but safe string 'test'
        # filter by add-on results and check number

        searchpage_obj.type_search_term('test')
        searchpage_obj.click_search()

        searchpage_obj.click_filter_libraries_link()

        # 20 items maximum per page
        label_count = min(searchpage_obj.library_count_label, 20)
        element_count = searchpage_obj.library_element_count()

        Assert.equal(label_count, element_count, 'Number of items displayed should match 20 or total number of results, whichever is smallest. This is due to pagination.')

    @xfail(reason = "Bug 695283 - Search not indexing add-ons")
    def test_clicking_addon_author_link_displays_author_profile(self, mozwebqa):
        # go to addon result and click author link

        homepage_obj = HomePage(mozwebqa)
        userpage_obj = UserPage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        addon_name = searchpage_obj.addon(1).name
        author_name = searchpage_obj.addon(addon_name).author_name
        searchpage_obj.addon(addon_name).click_author()
        Assert.equal(userpage_obj.author_name, author_name)

    def test_clicking_library_author_link_displays_author_profile(self, mozwebqa):

        # go to library result and click author link
        homepage_obj = HomePage(mozwebqa)
        userpage_obj = UserPage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()

        library_name = searchpage_obj.library(1).name
        author_name = searchpage_obj.library(library_name).author_name
        searchpage_obj.library(library_name).click_author()
        Assert.equal(userpage_obj.author_name, author_name)

    @xfail(reason = "Bug 691714: Page load event issue on Search results")
    def test_clicking_addon_source_displays_editor(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboard_obj = DashboardPage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)
        editorpage_obj = AddonEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login()
        dashboard_obj.header.click_search()

        addon_name = searchpage_obj.addon(1).name
        searchpage_obj.addon(addon_name).click_source()
        Assert.equal(editorpage_obj.addon_name, addon_name)

        searchpage_obj.delete_test_data()

    @xfail(reason = "Bug 691714: Page load event issue on Search results")
    def test_clicking_library_source_displays_editor(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)
        loginpage_obj = LoginPage(mozwebqa)
        dashboard_obj = DashboardPage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)
        editorpage_obj = LibraryEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        homepage_obj.header.click_signin()
        loginpage_obj.login()
        dashboard_obj.header.click_search()

        library_name = searchpage_obj.library(1).name
        searchpage_obj.library(library_name).click_source()
        Assert.equal(editorpage_obj.library_name, library_name)

        searchpage_obj.delete_test_data()
