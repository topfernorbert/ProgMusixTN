import time
import mysql.connector
from ProgMusix.configs.general_model import GeneralPage
from ProgMusix.configs.testdata import TESTDATA
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint

class ProgMusix(GeneralPage):

    def __init__(self, browser):
        super().__init__(browser, "http://localhost:4200")

    # Menu buttons:
    def menu_login_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@id="regLogin"]')

    def menu_logout(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_logOut"]')

    def menu_profile(self):
        return self.browser.find_element(By.XPATH, '//button[@id="profile"]')

    def menu_cart(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_myCart"]')

    def menu_location(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_location"]')

    def menu_search(self):
        return self.browser.find_element(By.XPATH, '//button[@id="button_search"]')

    def filter_on(self):
        return self.browser.find_element(By.XPATH, '//div[@id="filter-on"]')

    def filter_off(self):
        return self.browser.find_element(By.XPATH, '//div[@id="filter-off"]')

    # Login/Registration page
    def btn_signin(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="sign_in"]')))

    def btn_createaccount(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="create_account"]')))

        # Login oldal - Bejelentkezés

    def login_btn(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))

    # Signing in:

    def username_login(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'username_input')))

    def password_login(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'password_input')))

    # Signing in, negative:

    def negative_username_login_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-form-field-label-1')))

    def negative_password_login_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-form-field-label-3')))

    def negative_login_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-error-0'))).text

    # Regisztráció, pozitív ág:

    def create_btn(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="create_account"]')))

    def email(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-2')))

    def username(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-3')))

    def password(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-4')))

    def password_again(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-5')))

    def register_btn(self):
        return WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))

    def succesfull_msg(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="success_message ng-star-inserted"]'))).text

    def recaptcha(self):
        return WebDriverWait(self.browser, 10).until(
            (EC.visibility_of_element_located((By.ID, 'recaptcha-anchor-label'))))

    # Regisztráció, negatív ág:

    def enter_email(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-form-field-label-5')))

    def invalid_email_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-error-0'))).text

    def enter_username(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-form-field-label-7')))

    def invalid_username_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-error-1'))).text

    def enter_password(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-form-field-label-9')))

    def invalid_password_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-error-2'))).text

    def enter_password_again(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, 'mat-form-field-label-11')))

    def tab_password_again_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-error-3'))).text

    def dif_password_againg_msg(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-error-3')))

    def disabled_submit_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@type="submit"]').get_attribute("disabled")

    def checkers_password(self):
        return self.browser.find_element(By.ID, 'checkers')

    # Kapcsolat oldal

    def sendmessage_btn(self):
        return self.browser.find_element(By.XPATH, '//button[@type="submit"]')

    def name_contact(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-52')))

    def email_contact(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-53')))

    def message_contact(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, 'mat-input-54')))

    # Contact
    def contact_btn(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'button_location')))

    def contact_name(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-0')))

    def contact_email(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-1')))

    def contact_field(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'mat-input-2')))

    def contact_send_btm(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))

    def contact_msg_succ(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="mat-dialog-content"]'))).text

    def map_icon(self):
        return self.browser.find_element(By.XPATH,
                                         '//div[@class="leaflet-pane leaflet-marker-pane"]/img[@role="button"]')

    def address(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="leaflet-popup-content"]'))).text

    def contact_send_btn(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@color="accent"]')))

    # Megerősítő email:

    def email_link_last_email(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="email_item"]')))[0]

    def activate_link(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[text()="Activate Now"]')))

    # Database:

    def last_msg_sql(self):
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="test1234",
            database="webshop"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT email, message, name FROM message ORDER BY id DESC LIMIT 1")
        return cursor.fetchall()

    def last_user_sql(self):
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="test1234",
            database="webshop"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT email, username FROM custom_user ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()

    def change_admin_sql(self):
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="test1234",
            database="webshop"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(custom_user_id) FROM user_role")
        max_user_id = cursor.fetchone()[0]
        cursor.execute("UPDATE user_role SET roles = 'ROLE_ADMIN' WHERE custom_user_id = %s", (max_user_id,))
        connection.commit()

    def registration_method(self):
        self.menu_login_btn().click()
        time.sleep(1)
        self.create_btn().click()
        self.email().send_keys(TESTDATA['email_p'])
        self.username().send_keys(TESTDATA['username_p'])
        self.password().send_keys(TESTDATA['password_p'])
        self.password_again().send_keys(TESTDATA['password_p'])
        time.sleep(3)
        self.register_btn().click()

    def registration(self):
        self.menu_login_btn().click()
        time.sleep(1)
        self.create_btn().click()

    def registration_invalid_name(self):
        self.registration()
        self.email().send_keys(TESTDATA['email_p'])
        self.username().send_keys("TN")
        self.password().send_keys(TESTDATA['password_p'])
        self.password_again().send_keys(TESTDATA['password_p'])
        time.sleep(3)
        self.register_btn().click()

    def registration_invalid_email(self):
        self.registration()
        self.email().send_keys('invalid.invalid.hu')
        self.username().send_keys(TESTDATA['username_p'])
        self.password().send_keys(TESTDATA['password_p'])
        self.password_again().send_keys(TESTDATA['password_p'])
        time.sleep(3)
        self.register_btn().click()

    def registration_invalid_password(self):
        self.registration()
        self.email().send_keys(TESTDATA['email_p'])
        self.username().send_keys(TESTDATA['username_p'])
        self.password().send_keys('asd')
        self.password_again().send_keys('asd')
        time.sleep(3)
        self.register_btn().click()

    def registration_dif_password(self):
        self.registration()
        self.email().send_keys(TESTDATA['email_p'])
        self.username().send_keys(TESTDATA['username_p'])
        self.password().send_keys(TESTDATA['password_p'])
        self.password_again().send_keys('asd')
        time.sleep(3)
        self.register_btn().click()

    def registration_long_email(self):
        self.registration()
        self.email().send_keys('nagyon-hosszu-felhasznalonev-ami-majdnem-elferi-de-meg-kell-hozza@endtest-mail.io')
        self.username().send_keys(TESTDATA['username_p'])
        self.password().send_keys(TESTDATA['password_p'])
        self.password_again().send_keys('asd')
        time.sleep(3)
        self.register_btn().click()


    def reg_TAB_method(self):
        self.menu_login_btn().click()
        self.create_btn().click()
        self.email().send_keys(Keys.TAB)
        self.username().send_keys(Keys.TAB)
        self.password().send_keys(Keys.TAB)
        self.password_again().send_keys(Keys.TAB)

    def reg_negative_method(self):
        self.menu_login_btn().click()
        self.create_btn().click()
        self.email().send_keys(TESTDATA['negative_email'])
        self.username().send_keys(TESTDATA['negative_username'])
        self.password().send_keys(TESTDATA['negative_password'])
        self.password_again().send_keys(TESTDATA['negative_password_again'])
        self.password_again().send_keys(Keys.TAB)

    def login_method_p(self):
        self.menu_login_btn().click()
        time.sleep(2)
        self.username_login().send_keys(TESTDATA['username_p'])
        self.password_login().send_keys(TESTDATA['password_p'])
        self.login_btn().click()


    def login_method_TAB_n(self):
        self.menu_login_btn().click()
        self.username_login().send_keys(Keys.TAB)
        self.password_login().send_keys(Keys.TAB)

    def login_method_n(self):
        self.menu_login_btn().click()
        self.username_login().send_keys(TESTDATA['negative_login_username'])
        self.password_login().send_keys(TESTDATA['negative_login_password'])
        self.login_btn().click()


    def reg_email(self):
        self.browser.switch_to.new_window()
        self.browser.get('https://app.endtest.io/mailbox?email=pm-tn@endtest-mail.io')
        time.sleep(1)
        self.browser.refresh()
        time.sleep(3)
        self.email_link_last_email().click()

# Vásárlással kapcsolatos műveletek:

    def purchase_method(self):
        self.menu_search().click()
        self.product_card_1_addtocart().click()
        self.product_card_3_addtocart().click()

    def purchase_random_method(self):
        self.menu_search().click()
        random_counter = randint(1, 22)
        time.sleep(2)
        buttons = self.product_all_add_btn()
        for i in range(min(random_counter, len(buttons))):
            buttons[i].click()

    def convert_method(self):
        price_ints = []
        for price_element in self.product_prices():
            price_text = price_element.text
            price_number = ''.join(filter(str.isdigit, price_text))
            try:
                elem_int = int(price_number)
                price_ints.append(elem_int)
            except ValueError:
                print(f"Could not convert price text '{price_text}' to an integer.")
        return price_ints

    def add_method(self):
        price_ints = self.convert_method()
        total = sum(price_ints)
        return total

    def paying_method(self):
        # self.login_method_p()
        self.menu_cart().click()
        self.checkout_btn().click()
        self.btn_step2().click()

        self.input_billing_name().clear()
        self.input_billing_taxnumber().clear()
        self.input_billing_zipnumber().clear()
        self.input_billing_city().clear()
        self.input_billing_address().clear()
        self.input_billing_name().send_keys(TESTDATA['contact_name'])
        self.input_billing_taxnumber().send_keys(TESTDATA['tax_p'])
        self.input_billing_zipnumber().send_keys(TESTDATA['zip_p'])
        self.input_billing_city().send_keys(TESTDATA['city_p'])
        self.input_billing_address().send_keys(TESTDATA['street_p'])
        self.btn_step3().click()

        self.input_shipping_name().clear()
        self.input_shipping_zipnumber().clear()
        self.input_shipping_city().clear()
        self.input_shipping_address().clear()
        self.input_shipping_name().send_keys(TESTDATA['contact_name'])
        self.input_shipping_zipnumber().send_keys(TESTDATA['zip_p'])
        self.input_shipping_city().send_keys(TESTDATA['city_p'])
        self.input_shipping_address().send_keys(TESTDATA['street_p'])
        self.btn_step4().click()

        self.input_delivery_info().clear()
        self.input_delivery_info().send_keys(TESTDATA['delivery_p'])
        self.btn_step5().click()
        self.btn_sendorder().click()



    def paying_method_negative_01_short(self):
        self.menu_cart().click()
        self.checkout_btn().click()

        self.input_username().clear()
        self.input_email().clear()
        self.input_phonenumber().clear()
        self.input_username().send_keys('asd')
        self.input_email().send_keys('asd')
        self.input_phonenumber().send_keys('asd')

    def paying_method_negative_02_short(self):
        self.btn_step2().click()
        self.input_billing_name().clear()
        self.input_billing_taxnumber().clear()
        self.input_billing_zipnumber().clear()
        self.input_billing_city().clear()
        self.input_billing_address().clear()
        self.input_billing_name().send_keys('asd')
        self.input_billing_taxnumber().send_keys('asd')
        self.input_billing_zipnumber().send_keys('asd')
        self.input_billing_city().send_keys('as')
        self.input_billing_address().send_keys('asd')

    def paying_method_negative_03_short(self):
        self.btn_step3().click()
        self.input_shipping_name().clear()
        self.input_shipping_zipnumber().clear()
        self.input_shipping_city().clear()
        self.input_shipping_address().clear()
        self.input_shipping_name().send_keys('asd')
        self.input_shipping_zipnumber().send_keys('asd')
        self.input_shipping_city().send_keys('as')
        self.input_shipping_address().send_keys('asd')

    def paying_method_negative_04_short(self):
        self.btn_step4().click()
        self.input_delivery_info().clear()
        self.input_delivery_info().send_keys('asd')
        self.btn_step5().click()

    def paying_method_negative_01_long(self):
        self.menu_cart().click()
        self.checkout_btn().click()

        self.input_username().clear()
        self.input_email().clear()
        self.input_phonenumber().clear()
        self.input_username().send_keys('asdasdasdasdasdasdasdasdasd')
        self.input_email().send_keys('asdasdasdasdasdasdasdasdasd')
        self.input_phonenumber().send_keys('asdasdasdasdasdasdasdasdasd')

    def paying_method_negative_02_long(self):
        self.btn_step2().click()
        self.input_billing_name().clear()
        self.input_billing_taxnumber().clear()
        self.input_billing_zipnumber().clear()
        self.input_billing_city().clear()
        self.input_billing_address().clear()
        self.input_billing_name().send_keys('asdasdasdasdasdasdasdasdasd')
        self.input_billing_taxnumber().send_keys('asdasdasdasdasdasdasdasdasd')
        self.input_billing_zipnumber().send_keys('asdasdasdasdasdasdasdasdasd')
        self.input_billing_city().send_keys('asdasdasdasdasdasdasdasdasd')
        self.input_billing_address().send_keys('asdasdasdasdasdasdasdasdasd')


        # def price_int1(self):
        #     price_text = self.product_prices()[0].text
        #     price_number = ''.join(filter(str.isdigit, price_text))
        #     return int(price_number)
        #
        # def price_int2(self):
        #     price_text = self.product_prices()[1].text
        #     price_number = ''.join(filter(str.isdigit, price_text))
        #     return int(price_number)
        #
        # def price_addresult(self):
        #     price1 = self.price_int1()
        #     price2 = self.price_int2()
        #     return price1 + price2

        # def last_purchase_sql(self):
        #     connection = mysql.connector.connect(
        #         host="localhost",
        #         port=3306,
        #         user="root",
        #         password="test1234",
        #         database="webshop"
        #     )
        #     cursor = connection.cursor()
        #     cursor.execute("Select * From purchase Order by id desc limit 1;")
        #     return cursor.fetchone()

#Lokátorok:

    def checkout_btn(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Check out"]')))

    def input_username(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.ID, 'formName_input')))

    def input_email(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="formEmail_input"]')))

    def input_phonenumber(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="formPhoneNumber_input"]')))

#Buttons:
    # FIZETÉS OLDAL - FORM

    def btn_backtothecart(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Back to the cart "]')))

    def btn_next(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Next"]')))

    def btn_back(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Back"]')))

    def btn_sendorder(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Send order "]')))

    def btn_step2(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="2"]')))

    def btn_step3(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="3"]')))

    def btn_step4(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="4"]')))

    def btn_step5(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="5"]')))

# TERMÉK OLDAL:

    def product_cards(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="col ng-star-inserted"]')))

    def product_card_1_addtocart(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="1"]/mat-card/mat-card-actions/button[@id="button_addToCart"]')))

    def product_card_3_addtocart(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="3"]/mat-card/mat-card-actions/button[@id="button_addToCart"]')))

    def product_all_add_btn(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//button[@id="button_addToCart"]')))


 #Billing:

    def input_billing_name(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="formName1_input"]')))

    def input_billing_taxnumber(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="formTaxNumber_input"]')))

    def input_billing_zipnumber(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="formZIP_input"]')))

    def input_billing_city(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="city_input"]')))

    def input_billing_address(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="adress_input"]')))

# SHIPPING:

    def input_shipping_name(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="shippingName_input"]')))

    def input_shipping_zipnumber(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="shippingZIP_input"]')))

    def input_shipping_city(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="shippingCity_input"]')))

    def input_shipping_address(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="shippingStreet_input"]')))

# DELIVERY

    def input_delivery_info(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="delivery_input"]')))

    # FIZETÉS OLDAL - SUCCESS

    def input_success_window(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//mat-dialog-container[@id="mat-dialog-0"]')))

    def input_success_message(self):
        return WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="mat-dialog-content"]')))

