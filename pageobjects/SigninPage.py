from selenium.webdriver.common.by import By
from browser import basepage


class SigninPage(basepage.BasePage):
    user = (By.ID, "UserName")
    pwd = (By.ID, "Password")
    signInButton = (By.XPATH, "//div[3]/div[3]/div/input")

    def enter_userName(self, userName):
        self.driver.find_element(*SigninPage.user).send_keys(userName)
        print("UserName - Entered!")

    def enter_passWord(self, pwd):
        elem = self.driver.find_element(*SigninPage.pwd)
        elem.send_keys(pwd)
        print("Password - Entered!")

    def click_signin(self):
        elem = self.driver.find_element(*SigninPage.signInButton)
        elem.click()
        print("Sign in Button - Clicked!")
