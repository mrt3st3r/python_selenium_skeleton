from selenium.webdriver.common.by import By
from browser import basepage


class LoginPage(basepage.BasePage):
    signIn = (By.XPATH, "//div[3]/div[3]/div/div/span")
    checkIn = (By.XPATH, "//div[3]/div[2]/div/div/span")

    def click_SignIn(self):
        elem = self.driver.find_element(*LoginPage.signIn)
        elem.click()

    def click_checkin(self):
        elem = self.driver.find_element(*LoginPage.checkIn)
        elem.click()




