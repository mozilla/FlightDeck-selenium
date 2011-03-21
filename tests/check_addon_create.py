#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
# -*- coding: latin_1 -*-
# -*- coding: unicode_escape -*-

from selenium import selenium
import unittest, time, re, string

class check_addon_create(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox /Applications/Firefox4.0b7/Firefox.app/Contents/MacOS/firefox-bin", "https://builder-addons.allizom.org/")
        self.selenium.start()
    
    def test_check_addon_create(self):
        sel = self.selenium
        sel.open("/")
        
        sel.click("signin")
        sel.wait_for_page_to_load("30000")
        sel.type("id_username", "amo.test.acc@gmail.com")
        sel.type("id_password", "qwertyasdf")
        sel.click("save")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=Mozilla Labs − Add-ons Builder")
        sel.wait_for_page_to_load("30000")
        #After signing in, click on the create add-on button on the home page
        sel.click("//a[@id='create_addon']/span")
        sel.wait_for_page_to_load("30000")
        
        #Click on the save button to save this add-on
        sel.click("package-save")
        a=sel.get_text("//section[@id='package-info']/h3[@id='ji-toggler']/a")
        addon_name_saved=string.strip(a)
        print addon_name_saved
        
        #Go to the dashboard and check that the label for this add-on should show 'initial'.
        sel.click("link=My Account")
        sel.wait_for_page_to_load("30000")
        label_initial=sel.get_text("//section[@id='app-content']/ul[1]/li[1]/h4")
        print label_initial
        self.assertEqual(label_initial,"initial")

        #Get the name of the addon that is on the top of the list. Then assert that this should be the same as the initial name.
        s=sel.get_text("//section[@id='app-content']/ul[1]/li[1]/h3")
        s=string.rsplit(s,"by")
        addon_name_present=string.strip(s[0])
        print addon_name_present
        self.assertEqual(addon_name_saved, addon_name_present)
        #if cmp(addon_name_saved,addon_name_present) == 0:
            #print "Addon present"
        #else:
            #print "Addon which was created is not present here."
            #return -1

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
