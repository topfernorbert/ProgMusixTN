from ProgMusix.configs.config import get_preconfigured_chrome_driver
from ProgMusix.page_model import ProgMusix
from ProgMusix.configs.testdata import TESTDATA
import time


class TestProgmusix:
    def setup_method(self):
        page = ProgMusix(get_preconfigured_chrome_driver())
        self.page = page
        page.open()

    # def teardown_method(self):
    #     self.page.close()

    def test_registration(self):
        self.page.registration_method()
        # Helyesen lettek kitöltve az adatok, elérhető a regisztrációs gomb:
        assert self.page.register_btn().is_enabled()
        # Regisztráció megerősítő üzenet megjelenik:
        assert self.page.succesfull_msg() == TESTDATA['succesful_msg']
        # Adatbázisban is megjelenik a regisztráció:
        assert TESTDATA['email_p'] and TESTDATA['username_p'] in self.page.last_user_sql()

    def test_regtest(self):
        self.page.registration()
        assert self.page.current_url() == "http://localhost:4200/registration"

    def test_reg_email(self):
        # Annak ellenőrzése, hogy megérkezik a visszaigazoló e-mail és tartalmazza a kattintható aktiváló linket
        self.page.reg_email()
        assert self.page.activate_link().is_displayed()
        self.page.activate_link().click()

    def test_login_positive(self):
        self.page.login_method_p()
        # A belépéshez szükséges gomb engedélyezve van-e:
        assert self.page.login_btn().is_enabled()


    def test_reg_TAB(self):
        self.page.reg_TAB_method()
        assert self.page.invalid_email_msg() == TESTDATA['TAB_email']
        assert self.page.enter_email().is_displayed()
        assert self.page.invalid_username_msg() == TESTDATA['TAB_username']
        assert self.page.enter_username().is_displayed()
        assert self.page.invalid_password_msg() == TESTDATA['TAB_password']
        assert self.page.enter_password().is_displayed()
        assert self.page.tab_password_again_msg() == TESTDATA['TAB_password_again']
        assert self.page.enter_password_again().is_displayed()
        assert self.page.disabled_submit_btn() == 'true'

    def test_reg_negative(self):
        self.page.reg_negative_method()
        # Helytelen formátumra való felszólító üzenetek megjelenése:
        assert self.page.invalid_email_msg() == TESTDATA['negative_email_msg']
        assert self.page.invalid_username_msg() == TESTDATA['negative_username_msg']
        assert self.page.invalid_password_msg() == TESTDATA['negative_password_msg']
        assert self.page.checkers_password().is_displayed()
        assert self.page.dif_password_againg_msg().text == TESTDATA['negative_password_again_msg']

#Csak a username kitöltése helytelen:
    def test_reg_invalid_username(self):
        self.page.registration_invalid_name()
        assert not self.page.register_btn().is_enabled()

#Csak az email cím formátuma helytelen:

    def test_reg_invalid_email(self):
        self.page.registration_invalid_email()
        assert not self.page.register_btn().is_enabled()

#Csak a jelszó formátuma helytelen:

    def test_reg_invalid_password(self):
        self.page.registration_invalid_password()
        assert not self.page.register_btn().is_enabled()

#Eltérő jelszómegerősítés:

    def test_reg_dif_password(self):
        self.page.registration_dif_password()
        assert not self.page.register_btn().is_enabled()

#81 karakteres email cím:

    def test_long_email(self):
        self.page.registration_long_email()
        assert not self.page.register_btn().is_enabled()




    def test_login_TAB(self):
        self.page.login_method_TAB_n()
        # Megjelennek-e az adatbekérő üzenetek, ha üresen maradnak a mezők:
        assert self.page.negative_username_login_msg().is_displayed()
        assert self.page.negative_password_login_msg().is_displayed()

    def test_login_negative(self):
        self.page.login_method_n()
        # Rossz email cím/jelszó megjelenése:
        assert self.page.negative_login_msg() == TESTDATA['negative_login_msg']

    def test_contact(self):
        self.page.contact_btn().click()
        self.page.map_icon().click()
        # Megjelenik-e a cím, ha rákattint a helyzetjelző ikonra:
        assert TESTDATA['address'] in self.page.address()
        self.page.contact_name().send_keys(TESTDATA['contact_name'])
        self.page.contact_email().send_keys(TESTDATA['contact_email'])
        self.page.contact_field().send_keys(TESTDATA['contact_field'])
        self.page.contact_send_btm().click()
        time.sleep(1)
        # Egyezik, megjelenik az adatbázisban a beírt név, email cím, üzenet szövege:
        assert all(field in self.page.last_msg_sql()[0] for field in
                   [TESTDATA['contact_name'], TESTDATA['contact_email'], TESTDATA['contact_field']])

    def test_paying(self):
        #Login
        self.page.login_method_p()
        #Kosárba helyezés:
        self.page.purchase_random_method()
        # Fizetés
        self.page.paying_method()      
    
    def test_last_user_del(self):
        self.page.last_user_del_sql()


