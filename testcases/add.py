from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from selenium.webdriver.chrome.options import Options

# constants
CHROME_PATH = '/Users/test/Downloads/p/chromedriver'
BASE_URL_TST = 'https://test.contact.co.nz/'
MAKE_CHANGES_PAGE_TITLE = 'Contact Energy | Power Company | For Home | Make Changes'
ADD_PROPERTY_SUCCESS_PAGE_TITLE = 'Add Property Success'
ADD_PROPERTY_SUCCESS_PAGE_URL = 'https://test.contact.co.nz/residential/my-details/add-property-success'

# test data
test_data_acc_no = '123456879'
test_data_address = '2 Burton Way, Bishopdale, Nelson 7011'
test_data_emailaddress = 'AutoTest@contact.co.nz'
test_data_first_name = 'my first name'
test_data_last_name = 'my last name'
test_data_phone_no = '099876543'
test_data_dob = '18/03/1977'
test_data_move_out_date = '12/12/2020'
test_data_bank_acc = '9876543219876543'

# elements

# first page elements
add_property_xpath_elem = '//*[@id="user-journey-actions-form"]/div[2]/div/div/div[2]/label'
acc_no_id_elem = 'AccountNumber'
address_xpath_elem = '//*[contains(@id, "AddressPicker-")]'
electricity_css_elem = '.ELEC .cta-inner-wrapper'
no_of_people_css_elem = '.required-field > .radio:nth-child(2) > label'
selectedPlan_linkText_elem = 'POPULAR'
choosePlan_linkText_elem = 'Choose plan'
emailaddress_id_elem = 'Customer[CustomerInfo][EmailAddress]'
clickContinue_linkText_elem = 'Continue'


# secound page elements
title_css_elem = '.list-items-4 > .radio:nth-child(2) > label'
first_name_id_elem = 'Customer[CustomerInfo][FirstName]'
last_name_id_elem = 'Customer[CustomerInfo][LastName]'
secound_page_emailaddress_id_elem = 'Customer[CustomerInfo][EmailAddress]'
phone_number_id_elem = 'Customer[CustomerInfo][PhoneNumber]'
birth_date_id_elem = 'Customer[CustomerInfo][DateOfBirth]'
move_out_date_id_elem = 'Property[MoveInfo][MoveInDate]'
not_a_batch_css_elem = '.row:nth-child(5) .radio:nth-child(2) > label'
no_vulnerable_person_css_elem = ".row:nth-child(7) .radio:nth-child(2) > label"
no_medically_dependant_person_css_elem = '.bkgd-swap > .row .required-field .radio:nth-child(2) > label'
no_hazards_css_elem = '.checkbox:nth-child(4) > label'
bank_acc_id_elem = 'Promotion[DirectDebitDetails][BankAccountNumber]'
bank_acc_ts_and_cs_css_elem = '.col-xs-12 > .checkbox > label'
bill_monthly_period_css_elem = '.tickbutton-list > .radio:nth-child(4) > label'
plan_ts_and_cs_css_elem = '.row:nth-child(3) > .col-sm-12 > .required-field'
accept_general_ts_and_cs_css_elem = '.row:nth-child(4) .required-field > label'
join_button_css_elem = '.btn-default'

def wait_for_elem(x):
    time.sleep(x)

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.maximize_window()
driver.get(BASE_URL_TST+"residential/make-changes")
driver.implicitly_wait(60)  # seconds
t1 = time.time()
print('Test: -> Regression Test for Add a Property.\n Test Started!')
#  asserting the 'make changes' page title
assert MAKE_CHANGES_PAGE_TITLE in driver.title

#  select add a property
addProperty = driver.find_element_by_xpath(add_property_xpath_elem)
addProperty.click()
print('Add a property Selected!')

wait_for_elem(2)
#  enter acc no
accNo = driver.find_element_by_id(acc_no_id_elem)
accNo.send_keys(test_data_acc_no)
print('Account Number entered!')

#  enter address
addressPicker = driver.find_element_by_xpath(address_xpath_elem)
addressPicker.send_keys(test_data_address)
wait_for_elem(5)
addressPicker.send_keys(Keys.ARROW_DOWN)
addressPicker.send_keys(Keys.RETURN)
print('Address Picked!')

wait_for_elem(3)
# choose service
electricity = driver.find_element_by_css_selector(electricity_css_elem)
electricity.click()
print('Electricity Selected!')

wait_for_elem(3)
# No of people
no_of_people = driver.find_element_by_css_selector(no_of_people_css_elem)
no_of_people.click()
print('Number of people Selected!')

wait_for_elem(3)
selectedPlan = driver.find_element_by_link_text(selectedPlan_linkText_elem)
selectedPlan.click()
print('POPULAR plan - Selected!')

wait_for_elem(3)
#  choose plan
choosePlan = driver.find_element_by_link_text(choosePlan_linkText_elem)
choosePlan.click()
print('plan - Selected!')

wait_for_elem(3)
#  enter email address
emailAddress = driver.find_element_by_id(emailaddress_id_elem)
emailAddress.send_keys(test_data_emailaddress)
print('email address entered!')


wait_for_elem(5)
# click on continue to go to the next page
clickContinue = driver.find_element_by_link_text(clickContinue_linkText_elem)
clickContinue.click()
print('clicked continue!')

# waiting for the next page to be loaded so the first element can be accessed
wait_for_elem(5)
print(10*'-' + ' SECOND_PAGE (About You) ' + 10*'-')

title = driver.find_element_by_css_selector(title_css_elem)
title.click()
print('salutation/title - Selected!')

firstName = driver.find_element_by_id(first_name_id_elem)
firstName.send_keys(test_data_first_name)
print('first name -  entered!')

lastName = driver.find_element_by_id(last_name_id_elem)
lastName.send_keys(test_data_last_name)
print('last name -  entered!')

emailaddress = driver.find_element_by_id(secound_page_emailaddress_id_elem)
emailaddress.clear()
emailaddress.send_keys(test_data_emailaddress)
print('email address -  entered!')

phoneNumber = driver.find_element_by_id(phone_number_id_elem)
phoneNumber.send_keys(test_data_phone_no)
print('phone Number -  entered!')

dob = driver.find_element_by_id(birth_date_id_elem) # click on address picker on the home page
dob.send_keys(test_data_dob)
print('DoB -  entered!')

#  moving out date
moving_out_date = driver.find_element_by_id(move_out_date_id_elem) # click on address picker on the home page
moving_out_date.send_keys(test_data_move_out_date)
print('Moving Date -  entered!')

# Is it a batch?
not_a_batch = driver.find_element_by_css_selector(not_a_batch_css_elem)
not_a_batch.click()
print('Is it a Batch? No - Selected!')

wait_for_elem(2)
# No vulnerable person
no_vulnerable_person = driver.find_element_by_css_selector(no_vulnerable_person_css_elem)
no_vulnerable_person.click()
print('No vulnerable person - Selected!')


# No medically dependant
no_medically_dependent_person = driver.find_element_by_css_selector(no_medically_dependant_person_css_elem)
no_medically_dependent_person.click()
print('No medically dependant person - Selected!')

no_hazards = driver.find_element_by_css_selector(no_hazards_css_elem)
no_hazards.click()
print('No hazard - Selected!')

# entering bank acc no
bank_acc = driver.find_element_by_id(bank_acc_id_elem)
bank_acc.click()
wait_for_elem(2)
bank_acc.send_keys(test_data_bank_acc)
print('Bank account -  entered!')

# bank acc Ts & Cs
bank_acc_ts_and_cs = driver.find_element_by_css_selector(bank_acc_ts_and_cs_css_elem)
bank_acc_ts_and_cs.click()
print('agreed on Ts&Cs - Selected!')

# bill period
bill_period = driver.find_element_by_css_selector(bill_monthly_period_css_elem)
bill_period.click()
print('Monthly bill period Selected!')

wait_for_elem(2)
# accepting Ts & Cs of the plan
plan_ts_and_cs = driver.find_element_by_css_selector(plan_ts_and_cs_css_elem)
plan_ts_and_cs.click()
print("agreed on plan's Ts&Cs - Selected!")

wait_for_elem(2)
# accepting general Ts & Cs
accept_general_ts_and_cs = driver.find_element_by_css_selector(accept_general_ts_and_cs_css_elem)
accept_general_ts_and_cs.click()
print('agreed on general Ts&Cs - Selected!')

wait_for_elem(5)
# clicking on Join up now button
join_button = driver.find_element_by_css_selector(join_button_css_elem)
join_button.click()


wait_for_elem(5)
assert driver.title == ADD_PROPERTY_SUCCESS_PAGE_TITLE
assert driver.current_url == ADD_PROPERTY_SUCCESS_PAGE_URL
total_time_taken = time.time() - t1

print("Test Completed with Success!!")
print(f"Total time taken: {round(total_time_taken,2)} Seconds!")
driver.close()
