import fd_home_page




class TestActionChain():

    def test_click_create_addon(self, mozwebqa):
        homepage_obj = fd_home_page.HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        
        homepage_obj.header.click_create_addon()