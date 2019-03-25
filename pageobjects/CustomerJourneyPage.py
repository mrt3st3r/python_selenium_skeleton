import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser import basepage
from values import strings


class CustomerJourneyPage(basepage.BasePage):
    user = (By.ID, "UserName")
    pwd = (By.ID, "Password")
    signInButton = (By.XPATH, "//div[3]/div[3]/div/input")

    # Elements

    # make- changes page elements
    add_property_xpath_elem = (By.XPATH, '//*[@id="user-journey-actions-form"]/div[2]/div/div/div[2]/label')
    acc_no_id_elem = (By.ID, 'AccountNumber')
    address_xpath_elem = (By.XPATH, '//*[contains(@id, "AddressPicker-")]')
    electricity_css_elem = (By.CSS_SELECTOR, '.ELEC .cta-inner-wrapper')
    no_of_people_css_elem = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(2) > label')
    selectedPlan_linkText_elem = (By.LINK_TEXT, 'POPULAR')
    choosePlan_linkText_elem = (By.LINK_TEXT, 'Choose plan')
    emailaddress_id_elem = (By.ID, 'Customer[CustomerInfo][EmailAddress]')
    clickContinue_linkText_elem = (By.LINK_TEXT, 'Continue')

    # about you page elements
    title_css_elem = (By.CSS_SELECTOR, '.list-items-4 > .radio:nth-child(2) > label')
    first_name_id_elem = (By.ID, 'Customer[CustomerInfo][FirstName]')
    last_name_id_elem = (By.ID, 'Customer[CustomerInfo][LastName]')
    aboutyou_page_emailaddress_id_elem = (By.ID, 'Customer[CustomerInfo][EmailAddress]')
    phone_number_id_elem = (By.ID, 'Customer[CustomerInfo][PhoneNumber]')
    birth_date_id_elem = (By.ID, 'Customer[CustomerInfo][DateOfBirth]')
    move_out_date_id_elem = (By.ID, 'Property[MoveInfo][MoveInDate]')
    not_a_batch_css_elem = (By.CSS_SELECTOR, '.row:nth-child(5) .radio:nth-child(2) > label')
    no_vulnerable_person_css_elem = (By.CSS_SELECTOR, ".row:nth-child(7) .radio:nth-child(2) > label")
    no_medically_dependant_person_css_elem = (By.CSS_SELECTOR, '.bkgd-swap > .row .required-field .radio:nth-child(2) > label')
    no_hazards_css_elem = (By.CSS_SELECTOR, '.checkbox:nth-child(4) > label')
    bank_acc_id_elem = (By.ID, 'Promotion[DirectDebitDetails][BankAccountNumber]')
    bank_acc_ts_and_cs_css_elem = (By.CSS_SELECTOR, '.col-xs-12 > .checkbox > label')
    bill_monthly_period_css_elem = (By.CSS_SELECTOR, '.tickbutton-list > .radio:nth-child(4) > label')
    plan_ts_and_cs_css_elem = (By.CSS_SELECTOR, '.row:nth-child(3) > .col-sm-12 > .required-field')
    accept_general_ts_and_cs_css_elem = (By.CSS_SELECTOR, '.row:nth-child(4) .required-field > label')
    join_button_css_elem = (By.CSS_SELECTOR, '.btn-default')

    def add_property(self):
        self.driver.find_element(*CustomerJourneyPage.add_property_xpath_elem).click()
        print("Add property - Selected!")

    def enter_account_no(self, accNo):
        elem = self.driver.find_element(*CustomerJourneyPage.acc_no_id_elem)
        elem.send_keys(accNo)
        print("Account Number - Entered!")

    def pick_address(self, address):
        elem = self.driver.find_element(*CustomerJourneyPage.address_xpath_elem)
        elem.send_keys(address)
        time.sleep(5)
        elem.send_keys(Keys.ARROW_DOWN)
        elem.send_keys(Keys.RETURN)
        print('Address Picked!')

    def select_electricity(self):
        elem = self.driver.find_element(*CustomerJourneyPage.electricity_css_elem)
        elem.click()
        print('Electricity Selected!')

    def select_no_of_people_1_person(self):
        elem = self.driver.find_element(*CustomerJourneyPage.no_of_people_css_elem)
        elem.click()
        print('Number of people (1 person) Selected!')

    def select_electricity(self):
        elem = self.driver.find_element(*CustomerJourneyPage.electricity_css_elem)
        elem.click()
        print('Electricity Selected!')

    def select_plan(self):
        elem = self.driver.find_element(*CustomerJourneyPage.selectedPlan_linkText_elem)
        elem.click()
        print('POPULAR plan - Selected!')

    def choose_plan(self):
        elem = self.driver.find_element(*CustomerJourneyPage.choosePlan_linkText_elem)
        elem.click()
        print('plan - Selected!')

    def enter_email_address(self, email):
        elem = self.driver.find_element(*CustomerJourneyPage.emailaddress_id_elem)
        elem.send_keys(email)
        print('email address entered!')

    def click_continue_make_changes_page(self):
        elem = self.driver.find_element(*CustomerJourneyPage.clickContinue_linkText_elem)
        elem.click()
        print('clicked Continue!')

    def select_title(self):
        elem = self.driver.find_element(*CustomerJourneyPage.title_css_elem)
        elem.click()
        print('salutation/title - Selected!')

    def enter_first_name(self, fname):
        elem = self.driver.find_element(*CustomerJourneyPage.first_name_id_elem)
        elem.send_keys(fname)
        print('first name - Selected!')

    def enter_last_name(self, lname):
        elem = self.driver.find_element(*CustomerJourneyPage.last_name_id_elem)
        elem.send_keys(lname)
        print('last name - Selected!')

    def enter_emailAddress_abouyou_page(self, email):
        elem = self.driver.find_element(*CustomerJourneyPage.aboutyou_page_emailaddress_id_elem)
        elem.clear()
        elem.send_keys(email)
        print('email address - Entered!')

    def enter_phone_number(self, phone):
        elem = self.driver.find_element(*CustomerJourneyPage.phone_number_id_elem)
        elem.send_keys(phone)
        print('phone number - Entered!')

    def enter_birth_date(self, dob):
        elem = self.driver.find_element(*CustomerJourneyPage.birth_date_id_elem)
        elem.send_keys(dob)
        print('Date of Birth - Entered!')

    def enter_move_out_date(self, move_date):
        elem = self.driver.find_element(*CustomerJourneyPage.move_out_date_id_elem)
        elem.send_keys(move_date)
        print('Moving Date - Entered!')

    def select_no_batch(self):
        elem = self.driver.find_element(*CustomerJourneyPage.not_a_batch_css_elem)
        elem.click()
        print('Is it a Batch? No - Selected!')

    def select_no_vulnerable_person(self):
        elem = self.driver.find_element(*CustomerJourneyPage.no_vulnerable_person_css_elem)
        elem.click()
        print('No vulnerable person - Selected!')

    def select_no_medically_dependant_person(self):
        elem = self.driver.find_element(*CustomerJourneyPage.no_medically_dependant_person_css_elem)
        elem.click()
        print('No medically dependant person - Selected!')

    def select_no_hazards(self):
        elem = self.driver.find_element(*CustomerJourneyPage.no_hazards_css_elem)
        elem.click()
        print('No hazard - Selected!')

    def enter_bank_account(self, bank_acc):
        elem = self.driver.find_element(*CustomerJourneyPage.bank_acc_id_elem)
        elem.click()
        time.sleep(2)
        elem.send_keys(bank_acc)
        print('Bank account -  entered!')

    def select_bank_acc_ts_and_cs(self):
        elem = self.driver.find_element(*CustomerJourneyPage.bank_acc_ts_and_cs_css_elem)
        elem.click()
        print('agreed on Ts&Cs - Selected!')

    def select_monthly_bill_period(self):
        elem = self.driver.find_element(*CustomerJourneyPage.bill_monthly_period_css_elem)
        elem.click()
        print('Monthly bill period Selected!')

    def accept_plan_ts_and_cs(self):
        time.sleep(2)
        elem = self.driver.find_element(*CustomerJourneyPage.plan_ts_and_cs_css_elem)
        elem.click()
        print("agreed on plan's Ts&Cs - Selected!")

    def accept_plan_ts_and_cs(self):
        time.sleep(2)
        elem = self.driver.find_element(*CustomerJourneyPage.plan_ts_and_cs_css_elem)
        elem.click()
        print("agreed on plan's Ts&Cs - Selected!")

    def accept_general_ts_and_cs(self):
        time.sleep(2)
        elem = self.driver.find_element(*CustomerJourneyPage.accept_general_ts_and_cs_css_elem)
        elem.click()
        print('agreed on general Ts&Cs - Selected!')

    def click_join_now_button(self):
        time.sleep(5)
        elem = self.driver.find_element(*CustomerJourneyPage.join_button_css_elem)
        elem.click()
        print('Join Now button - Clicked!!')

