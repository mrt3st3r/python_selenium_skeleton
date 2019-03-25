import time
import unittest
from selenium import webdriver
from pageobjects import CustomerJourneyPage
from values import strings


def wait_for_elem(x):
    time.sleep(x)


class Test_AddProperty(unittest.TestCase):

    def setUp(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(strings.chromePath)
        self.driver.implicitly_wait(60)  # seconds
        self.driver.maximize_window()

        # , options=chrome_options
        self.driver.get(strings.base_url + "residential/make-changes")

    def test_customer_journey_add_property(self):
        driver = self.driver
        addpropertypage = CustomerJourneyPage.CustomerJourneyPage(driver)
        t1 = time.time()
        print('Test: -> Regression Test for Add a Property.\n Test Started!')
        #  asserting the 'make changes' page title
        assert strings.MAKE_CHANGES_PAGE_TITLE in driver.title

        #  select add a property
        addpropertypage.add_property()
        wait_for_elem(2)

        #  enter acc no
        addpropertypage.enter_account_no(strings.test_data_acc_no)
        wait_for_elem(3)
        #  enter address
        addpropertypage.pick_address(strings.test_data_address)
        wait_for_elem(3)
        # choose service
        addpropertypage.select_electricity()
        wait_for_elem(3)
        # No of people
        addpropertypage.select_no_of_people_1_person()
        wait_for_elem(3)
        addpropertypage.select_plan()
        wait_for_elem(3)
        #  choose plan
        addpropertypage.choose_plan()
        wait_for_elem(3)
        #  enter email address
        addpropertypage.enter_email_address(strings.test_data_emailaddress)
        wait_for_elem(5)
        #  click continue
        addpropertypage.click_continue_make_changes_page()

        # waiting for the next page to be loaded so the first element can be accessed
        wait_for_elem(5)
        print(10 * '-' + ' SECOND_PAGE (About You) ' + 10 * '-')
        print("Entering personal details")
        addpropertypage.select_title()
        addpropertypage.enter_first_name(strings.test_data_first_name)
        addpropertypage.enter_last_name(strings.test_data_last_name)
        addpropertypage.enter_emailAddress_abouyou_page(strings.test_data_emailaddress)
        addpropertypage.enter_phone_number(strings.test_data_phone_no)
        addpropertypage.enter_birth_date(strings.test_data_dob)
        addpropertypage.enter_move_out_date(strings.test_data_move_out_date)
        addpropertypage.select_no_batch()


        wait_for_elem(2)
        # No vulnerable person
        addpropertypage.select_no_vulnerable_person()
        addpropertypage.select_no_medically_dependant_person()
        addpropertypage.select_no_hazards()
        addpropertypage.enter_bank_account(strings.test_data_bank_acc)
        addpropertypage.select_bank_acc_ts_and_cs()
        addpropertypage.select_monthly_bill_period()
        addpropertypage.accept_plan_ts_and_cs()
        addpropertypage.accept_general_ts_and_cs()
        addpropertypage.click_join_now_button()

        print(10 * '-' + ' Waiting for Success_PAGE ' + 10 * '-')
        wait_for_elem(5)
        assert driver.title == strings.ADD_PROPERTY_SUCCESS_PAGE_TITLE
        assert driver.current_url == strings.ADD_PROPERTY_SUCCESS_PAGE_URL
        print("Add Property Success Page - Verified!")

        total_time_taken = time.time() - t1
        print("Add property Test Completed with Success!!")
        print(f"Total time taken: {round(total_time_taken, 2)} Seconds!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()




