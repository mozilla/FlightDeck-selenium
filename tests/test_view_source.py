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
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.library_editor_page import LibraryEditorPage
from pages.addon_editor_page import AddonEditorPage
from unittestzero import Assert


class TestViewSource():

    def test_view_addon_source(self, mozwebqa):
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
