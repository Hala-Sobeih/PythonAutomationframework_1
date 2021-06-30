import allure
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
from allure_commons.types import AttachmentType

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
       driver = self.driver
       driver.get("utils.URL")

       login = LoginPage(driver)
       login.enter_username(utils.USERNAME)
       login.enter_password(utils.PASSWORD)
       login.click_login()

       #driver.find_element_by_id("txtUsername").send_keys("Admin")
       #driver.find_element_by_id("txtPassword").send_keys("admin123")
       #driver.find_element_by_id("btnLogin").click()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            allure.attach(self.drive.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("no exceptions occurred")

        finally:
            print("Im inside finally block")







