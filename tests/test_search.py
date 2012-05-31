#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home_page import HomePage
from pages.editor_page import AddonEditorPage
from pages.editor_page import LibraryEditorPage
from pages.user_page import UserPage
from unittestzero import Assert
import pytest


class TestSearch:

    @pytest.mark.nondestructive
    def test_search_by_addon_name_returns_addon(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()

        #create a new addon with the valid criteria (version not initial)
        homepage_obj = dashboard_obj.header.click_home_logo()
        addonpage_obj = homepage_obj.click_create_addon_btn()
        addonpage_obj.type_package_version('searchable')
        addonpage_obj.click_save()
        searchterm = addonpage_obj.package_name

        homepage_obj = addonpage_obj.header.click_home_logo()
        searchpage_obj = homepage_obj.header.click_search()

        searchpage_obj.search_until_package_exists(searchterm, searchpage_obj.addon(searchterm))
        Assert.true(searchpage_obj.addon(searchterm).is_displayed, '%s not found before timeout' % searchterm)

        searchpage_obj.delete_test_data()

    @pytest.mark.nondestructive
    def test_search_by_library_name_returns_library(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()

        #create a new library with the valid criteria (version not initial)
        homepage_obj = dashboard_obj.header.click_home_logo()
        libpage_obj = homepage_obj.click_create_lib_btn()
        libpage_obj.type_package_version('searchable')
        libpage_obj.click_save()
        searchterm = libpage_obj.package_name

        homepage_obj = libpage_obj.header.click_home_logo()
        searchpage_obj = homepage_obj.header.click_search()

        searchpage_obj.search_until_package_exists(searchterm, searchpage_obj.library(searchterm))
        Assert.true(searchpage_obj.library(searchterm).is_displayed, '%s not found before timeout' % searchterm)

        searchpage_obj.delete_test_data()

    @pytest.mark.nondestructive
    def test_search_partial_addon_name_returns_addon(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        # get addon name, split string in half and search with it
        # results should be returned including the original addon

        top_addon_name = searchpage_obj.addon(1).name
        search_string = top_addon_name[:4]
        searchpage_obj.type_search_term(search_string)
        searchpage_obj.click_search()

        if searchpage_obj.is_see_all_matching_addons_visible:
            searchpage_obj.click_see_all_matching_addons()

        Assert.true(searchpage_obj.addons_element_count >= 1)
        Assert.true(searchpage_obj.addon(top_addon_name).is_displayed, 'Addon \'%s\' not found' % top_addon_name)

    @pytest.mark.nondestructive
    def test_search_partial_library_name_returns_library(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        # get library name, split string in half and search with it
        # results should be returned including the original addon

        top_library_name = searchpage_obj.library(1).name
        search_string = top_library_name[:4]
        searchpage_obj.type_search_term(search_string)
        searchpage_obj.click_search()

        if searchpage_obj.is_see_all_matching_libraries_visible:
            searchpage_obj.click_see_all_matching_libraries()

        Assert.greater_equal(searchpage_obj.library_element_count, 1)
        Assert.true(searchpage_obj.library(top_library_name).is_displayed, 'Library \'%s\' not found' % top_library_name)

    @pytest.mark.nondestructive
    def test_empty_search_returns_all_results(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        # search with a zero length string should still return results
        # default display is for 5 addons/5 libraries
        # same as filtering by 'Combined'

        searchpage_obj.clear_search()
        searchpage_obj.click_search()

        Assert.equal(searchpage_obj.addons_element_count, 5)
        Assert.equal(searchpage_obj.library_element_count, 5)

    @pytest.mark.nondestructive
    def test_search_addon_filter_results_match(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        # search with a generic but safe string 'test'
        # filter by add-on results and check number

        searchpage_obj.type_search_term('test')
        searchpage_obj.click_search()

        searchpage_obj.click_filter_addons_link()

        # 20 items maximum per page
        label_count = min(searchpage_obj.addons_count_label, 20)
        element_count = searchpage_obj.addons_element_count
        library_count = searchpage_obj.library_element_count

        Assert.equal(label_count, element_count, 'Number of items displayed should match 20 or total number of results, whichever is smallest. This is due to pagination.')

        Assert.equal(library_count, 0, 'Number of library elements shown should be 0 when add-on filter is enabled.')

    @pytest.mark.nondestructive
    def test_search_library_filter_results_match(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        # search with a generic but safe string 'test'
        # filter by add-on results and check number

        searchpage_obj.type_search_term('test')
        searchpage_obj.click_search()

        searchpage_obj.click_filter_libraries_link()

        # 20 items maximum per page
        label_count = min(searchpage_obj.library_count_label, 20)
        element_count = searchpage_obj.library_element_count

        Assert.equal(label_count, element_count, 'Number of items displayed should match 20 or total number of results, whichever is smallest. This is due to pagination.')

    @pytest.mark.nondestructive
    def test_clicking_addon_author_link_displays_author_profile(self, mozwebqa):
        # go to addon result and click author link

        homepage_obj = HomePage(mozwebqa)
        userpage_obj = UserPage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        addon_name = searchpage_obj.addon(1).name
        author_name = searchpage_obj.addon(addon_name).author_name
        searchpage_obj.addon(addon_name).click_author()
        Assert.equal(userpage_obj.author_name.lower(), author_name)

    @pytest.mark.nondestructive
    def test_clicking_library_author_link_displays_author_profile(self, mozwebqa):

        # go to library result and click author link
        homepage_obj = HomePage(mozwebqa)
        userpage_obj = UserPage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        library_name = searchpage_obj.library(1).name
        author_name = searchpage_obj.library(library_name).author_name
        searchpage_obj.library(library_name).click_author()
        Assert.equal(userpage_obj.author_name.lower(), author_name)

    @pytest.mark.xfail(reason="Bug 723042 - Incorrect addon name displayed")
    def test_clicking_addon_source_displays_editor(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        editorpage_obj = AddonEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()
        searchpage_obj = dashboard_obj.header.click_search()

        addon_name = searchpage_obj.addon(1).name
        searchpage_obj.addon(addon_name).click()
        Assert.equal(editorpage_obj.package_name, addon_name)

        searchpage_obj.delete_test_data()

    @pytest.mark.nondestructive
    def test_clicking_library_source_displays_editor(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        editorpage_obj = LibraryEditorPage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()
        searchpage_obj = dashboard_obj.header.click_search()

        library_name = searchpage_obj.library(1).name
        searchpage_obj.library(library_name).click()
        Assert.equal(editorpage_obj.package_name, library_name)

        searchpage_obj.delete_test_data()

    @pytest.mark.native
    @pytest.mark.nondestructive
    def test_copies_slider_filters_results(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        initial_addon_count = searchpage_obj.addons_count_label
        initial_library_count = searchpage_obj.library_count_label
        searchpage_obj.move_copies_slider(1)

        Assert.true(initial_addon_count > searchpage_obj.addons_count_label)
        Assert.true(initial_library_count > searchpage_obj.library_count_label)

    @pytest.mark.native
    @pytest.mark.nondestructive
    def test_used_packages_slider_filters_results(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()
        searchpage_obj.click_filter_libraries_link()

        initial_library_count = searchpage_obj.library_count_label
        searchpage_obj.move_used_packages_slider(10)

        Assert.true(initial_library_count > searchpage_obj.library_count_label)

    @pytest.mark.native
    @pytest.mark.nondestructive
    def test_activity_slider_filters_results(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        initial_addon_count = searchpage_obj.addons_count_label
        initial_library_count = searchpage_obj.library_count_label
        searchpage_obj.move_activity_slider(1)

        Assert.true(initial_addon_count > searchpage_obj.addons_count_label)
        Assert.true(initial_library_count > searchpage_obj.library_count_label)

    @pytest.mark.nondestructive
    @pytest.mark.xfail(reason="Bug 738469 - Default sort order says 'Activity', but doesn't actually match 'Activity' search-sort order/results")
    def test_default_search_order_is_by_activity(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        searchpage_obj = homepage_obj.header.click_search()

        searchpage_obj.type_search_term('addon')
        searchpage_obj.click_search()

        searchpage_obj.click_see_all_matching_addons()

        Assert.equal('Activity', searchpage_obj.current_sort_method)

        addons_activity_property_list = []
        while searchpage_obj.paginator.is_next_visible:
            for lookup in range(1, searchpage_obj.addons_element_count + 1):
                addons_activity_property_list.append(
                        searchpage_obj.addon(lookup).activity_rating)

            Assert.is_sorted_descending(addons_activity_property_list, 'The addons are not sorted by Activity')
            searchpage_obj.paginator.next()
