#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.library_editor_page import LibraryEditorPage
from pages.addon_editor_page import AddonEditorPage
from unittestzero import Assert


class TestViewSource:

    def test_view_source_addon(self, mozwebqa):
        #This test is to check viewing the source of an addon while not logged in
        homepage_obj = HomePage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)
        addoneditor_obj = AddonEditorPage(mozwebqa)

        #Go to search page and click view source on the first addon listed
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()
        
        searchpage_obj.addon(1).click()

        Assert.true(addoneditor_obj.tab(1).selected)        
        Assert.not_none(addoneditor_obj.tab(1).content)

    def test_view_source_library(self, mozwebqa):
        #This test is to check viewing the source of a library while not logged in
        homepage_obj = HomePage(mozwebqa)
        searchpage_obj = SearchPage(mozwebqa)
        libraryeditor_obj = LibraryEditorPage(mozwebqa)

        #Go to search page and click view source on the first library listed
        homepage_obj.go_to_home_page()
        homepage_obj.header.click_search()
        
        searchpage_obj.library(1).click()
        
        Assert.true(libraryeditor_obj.tab(1).selected)
        Assert.not_none(libraryeditor_obj.tab(1).content)
