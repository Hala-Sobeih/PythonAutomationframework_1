class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_css_selector = "#welcome"
        self.logout_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_css_selector(self.welcome_link_css_selector).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText ).click()



