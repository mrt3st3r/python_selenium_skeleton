import time
import unittest

from selenium import webdriver

from pageobjects import SigninPage
from values import strings


class Test_Signin(unittest.TestCase):

    def setUp(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(strings.chromePath)
        # , options=chrome_options
        self.driver.get(strings.base_url + "account/sign-in")

    def test_contact_signInPage_valid_user(self):
        driver = self.driver
        signinpage = SigninPage.SigninPage(driver)
        signinpage.enter_userName("1000059069@mailinator.com")
        signinpage.enter_passWord("Login@123")
        signinpage.click_signin()
        time.sleep(2)
        assert driver.title == "Contact Energy Online Login | My Account"

    def test_contact_signInPage_invalid_user(self):
        driver = self.driver
        signinpage = SigninPage.SigninPage(driver)
        signinpage.enter_userName("1000059069@mailinator.com")
        signinpage.enter_passWord("Invalid Password")
        signinpage.click_signin()
        time.sleep(2)
        assert driver.title != "Contact Energy Online Login | My Account"
        assert driver.title == "Account | Power Company | Account Sign In"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
