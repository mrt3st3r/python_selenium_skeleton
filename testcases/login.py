

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/Users/test/Downloads/p/chromedriver")
driver.maximize_window()
driver.get("https://test.contact.co.nz/account/sign-in")
driver.implicitly_wait(60) # seconds

print(driver.title)
assert driver.title == 'Account | Power Company | Account Sign In'
#  asserting the home page title

user = driver.find_element_by_id('UserName')
user.send_keys('blah@blah.com')
print('username entered!')

pwd = driver.find_element_by_id('Password')
pwd.send_keys('1234567898')
print('password entered!')

signIn = driver.find_element_by_xpath('//div[3]/div[3]/div/input')
signIn.click()
print('Click on Sign In button!')

print("BINGO!")
time.sleep(10000)
