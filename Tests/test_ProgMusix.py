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

    # def test_registration(self):
    #     self.page.registration_method()
    #     # Helyesen lettek kitöltve az adatok, elérhető a regisztrációs gomb:
    #     assert self.page.register_btn().is_enabled()
    #     # Regisztráció megerősítő üzenet megjelenik:
    #     assert self.page.succesfull_msg() == TESTDATA['succesful_msg']
    #     # Adatbázisban is megjelenik a regisztráció:
    #     assert TESTDATA['email_p'] and TESTDATA['username_p'] in self.page.last_user_sql()



    def test_reg_email(self):
        # Annak ellenőrzése, hogy megérkezik a visszaigazoló e-mail és tartalmazza a kattintható aktiváló linket
        self.page.reg_email()
        assert self.page.activate_link().is_displayed()
        self.page.activate_link().click()




#81 karakteres email cím:

    def test_long_email(self):
        self.page.registration_long_email()
        assert not self.page.register_btn().is_enabled()


    def test_login_TAB(self):
        time.sleep(1)
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




    # @pytest.mark.order(-1)
    # def test_last_user_del(self):
    #     self.page.last_user_del_sql()

    def test_postman1(self):
        self.page.postman_1()
        assert self.page.postman_1() == '[{"id":1,"name":"WOODWIND"},{"id":2,"name":"BRASS INSTRUMENTS"},{"id":3,"name":"PERCUSSION INSTRUMENTS"},{"id":4,"name":"KEYBOARD INSTRUMENTS"},{"id":5,"name":"GUITAR FAMILY"},{"id":6,"name":"BOWED STRINGS"},{"id":7,"name":"MISC"},{"id":14,"name":"TRADITIONAL"}]'


