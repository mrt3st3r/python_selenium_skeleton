import time
import unittest

from selenium import webdriver

from pageobjects import LoginPage

from values import strings


class TestMrT3st3r(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(strings.chromePath)
        self.driver.get(strings.base_url)


    def test_home_screen(self):
        driver = self.driver
        loginpage = LoginPage.LoginPage(driver)

        loginpage.click_SignIn()
        time.sleep(2)
        driver.back()
        loginpage.click_checkin()
        time.sleep(2)
        print('all done!')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
