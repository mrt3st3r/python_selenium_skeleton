

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/Users/test/Downloads/p/chromedriver")
driver.maximize_window()
driver.get("https://test.contact.co.nz/residential/find-a-plan")
driver.implicitly_wait(60) # seconds

print(driver.title)
#  asserting the home page title
assert "Contact Energy | Power Company | For Home | Find a Plan" in driver.title
addressPicker = driver.find_element_by_xpath('//*[contains(@id, "AddressPicker-")]') # click on address picker on the home page
addressPicker.send_keys('2 Burton Way, Bishopdale, Nelson 7011')
time.sleep(5) #TODO replace with smart wait
addressPicker.send_keys(Keys.ARROW_DOWN)
# addressPicker.send_keys(Keys.ARROW_DOWN)
addressPicker.send_keys(Keys.RETURN)
print('Address Picked!')
# time.sleep(10) #TODO replace with smart wait
electricity = driver.find_element_by_css_selector('.ELEC .cta-inner-wrapper') # click on address picker on the home page
electricity.click()
print('Electricity Selected!')
time.sleep(5)


no_of_people = driver.find_element_by_css_selector('.required-field > .radio:nth-child(2) > label') # click on address picker on the home page
no_of_people.click()
print('Number of people Selected!')
time.sleep(3)

selectedPlan = driver.find_element_by_link_text('POPULAR') # click on address picker on the home page
selectedPlan.click()
print('POPULAR plan - Selected!')
time.sleep(3)

choosePlan = driver.find_element_by_link_text('Choose plan') # click on address picker on the home page
choosePlan.click()
print('plan - Selected!')
time.sleep(3)

emailAddress = driver.find_element_by_id('Customer[CustomerInfo][EmailAddress]') # click on address picker on the home page
emailAddress.send_keys('AutoTest@contact.co.nz')
print('email address entered!')
time.sleep(5)

clickContinue = driver.find_element_by_link_text('Continue') # click on address picker on the home page
clickContinue.click()
print('clicked continue!')
# time.sleep(30)
# clickContinue.click()
# print('clicked continue! for the second time')
time.sleep(5)

#  ------------ second page -----------
title = driver.find_element_by_css_selector('.list-items-4 > .radio:nth-child(2) > label') # click on address picker on the home page
title.click()
print('salutation/title - Selected!')

firstName = driver.find_element_by_id('Customer[CustomerInfo][FirstName]') # click on address picker on the home page
firstName.send_keys('myFirstName')
print('first name -  entered!')

lastName = driver.find_element_by_id('Customer[CustomerInfo][LastName]') # click on address picker on the home page
lastName.send_keys('myLastName')
print('last name -  entered!')

emailaddress = driver.find_element_by_id('Customer[CustomerInfo][EmailAddress]') # click on address picker on the home page
emailaddress.clear()
emailaddress.send_keys('AutoTest@contact.co.nz')
print('email address -  entered!')

phoneNumber = driver.find_element_by_id('Customer[CustomerInfo][PhoneNumber]') # click on address picker on the home page
phoneNumber.send_keys('099876543')
print('phone Number -  entered!')

dob = driver.find_element_by_id('Customer[CustomerInfo][DateOfBirth]') # click on address picker on the home page
dob.send_keys('12/12/1980')
print('DoB -  entered!')

moved_house_no = driver.find_element_by_css_selector('.row:nth-child(3) .table-row .radio:nth-child(2) > label') # click on address picker on the home page
moved_house_no.click()
print('moved house? No - Selected!')


changing_supplier = driver.find_element_by_css_selector('.row:nth-child(1) > .reveal > .list-items-2 > .radio:nth-child(2) > label') # click on address picker on the home page
changing_supplier.click()
print('Changing energy supplier - Selected!')


no_vulnerable_person = driver.find_element_by_css_selector('.row:nth-child(8) .radio:nth-child(2) > label') # click on address picker on the home page
no_vulnerable_person.click()
print('No vulnerable person - Selected!')

no_medically_dependent_person = driver.find_element_by_css_selector('.bkgd-swap:nth-child(9) > .row .radio:nth-child(2) > label') # click on address picker on the home page
no_medically_dependent_person.click()
print('No medically dependant person - Selected!')

# #TODO following to be fixed
# boo = Select(driver.find_element_by_xpath('/html/body/div[2]/div/form/fieldset[2]/div/div[8]/div/div/div/div[1]/div[4]/label')) # click on address picker on the home page
# # ActionChains(driver).move_to_element_with_offset(boo,249,1).click().perform()
# # /html/body/div[2]/div/form/fieldset[2]/div/div[8]/div/div/div/div[1]/div[4]/label
# # ActionChains(driver).move_to_element_with_offset(boo,249,1).click().perform()
# time.sleep(10000)
# boo.click()
#
# boo.click()

# if no_hazard.get_attribute("type") == "checkbox":
#     print("great")
# else:
#     print("not a checkbox :(")
#     print(no_hazard.get_attribute("type"))
#     driver.find_element_by_link_text('No hazards').click()  # click on address picker on the home page
#     print('yessss')
#
# no_hazard.click() #   .checkbox:nth-child(4) > label
# no_hazard.click()
# print('No hazard - Selected!')

#TODO fix the below
bank_acc = driver.find_element_by_id('Promotion[DirectDebitDetails][BankAccountNumber]') # click on address picker on the home page
bank_acc.click()
time.sleep(2)
bank_acc.send_keys('9876543219876543')
print('Bank account -  entered!')
#
# ts_and_cs = driver.find_element_by_css_selector('.col-xs-12 > .checkbox > label') # click on address picker on the home page
# ts_and_cs.click()
# print('agreed on Ts&Cs - Selected!')
#
# weekly_bill = driver.find_element_by_css_selector('.list-items-3 > .radio:nth-child(2) > label') # click on address picker on the home page
# ts_and_cs.click()
# print('Weekly Bill - Selected!')
#
# plan_ts_and_cs = driver.find_element_by_css_selector('.list-items-3 > .radio:nth-child(2) > label') # click on address picker on the home page
# plan_ts_and_cs.click()
# print('agreed on Ts&Cs - Selected!')
#
# accept_general_ts_and_cs = driver.find_element_by_css_selector('.bkgd-swap:nth-child(2) .radio:nth-child(2) > label') # click on address picker on the home page
# plan_ts_and_cs.click()
# print('agreed on general Ts&Cs - Selected!')
#

print("BINGO!")
time.sleep(10000)
driver.close()

# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
