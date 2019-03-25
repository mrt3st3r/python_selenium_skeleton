import unittest

from selenium import webdriver

from pageobjects import SigninPage
from values import strings


class Test_Signin(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(strings.chromePath, options=chrome_options)
        self.driver.get(strings.base_url)

    def test_contact_signIn_Page(self):
        driver = self.driver
        signinpage = SigninPage.SigninPage(driver)
        signinpage.enter_userName("user@contact.co.nz")
        signinpage.enter_passWord("password")
        signinpage.click_signin()
        print("All Done!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
