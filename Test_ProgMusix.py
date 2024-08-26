from configs.config import get_preconfigured_chrome_driver
from page_model import ProgMusix
from configs.testdata import TESTDATA


class TestProgmusix:
    def setup_method(self):
        page = ProgMusix(get_preconfigured_chrome_driver())
        self.page = page
        page.open()
    def teardown_method(self):
        self.page.close()


# Regisztráció, majd bejelentkezés a megerősítő e-mailben kapott aktiváló linket használva.
#     def test_reg_positive(self):
#         self.page.registration_method()
#         self.page.new_tab_email()
#         #Helyesen lettek kitöltve az adatok, elérhető a regisztrációs gomb:
#         assert self.page.register_btn().is_enabled()
#         #Regisztráció megerősítő üzenet megjelenik:
#         assert self.page.succesfull_msg() == TESTDATA['succesful_msg']
#         #Adatbázisban is megjelenik a regisztráció:
#         assert TESTDATA['email_p'] and TESTDATA['username_p'] in self.page.last_user_sql()
#         #Regisztrációs e-mail ellenőrzése:
#         self.page.new_tab_email()
#         assert self.page.current_url() == TESTDATA["ProgMusix_URL"]


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
        #Helytelen formátumra való felszólító üzenetek megjelenése:
        assert self.page.invalid_email_msg() == TESTDATA['negative_email_msg']
        assert self.page.invalid_username_msg() == TESTDATA['negative_username_msg']
        assert self.page.invalid_password_msg() == TESTDATA['negative_password_msg']
        assert self.page.checkers_password().is_displayed()
        assert self.page.dif_password_againg_msg() == TESTDATA['negative_password_again_msg']
#
#     def test_login_positive(self):
#         self.page.login_method_p()
#         #A belépéshez szükséges gomb engedélyezve van-e:
#         assert self.page.login_btn().is_enabled()
#
#     def test_login_negative_and_TAB(self):
#         self.page.login_method_TAB_n()
#         #Megjelennek-e az adatbekérő üzenetek, ha üresen maradnak a mezők:
#         assert self.page.negative_username_login_msg().is_displayed()
#         assert self.page.negative_password_login_msg().is_displayed()
#         self.page.login_method_n()
#         #Rossz email cím/jelszó megjelenése:
#         assert self.page.negative_login_msg() == TESTDATA['negative_login_msg']
#
# #US:TE24FEBW1-41, Kapcsolat menüpont.
#
#     def test_contact(self):
#         self.page.contact_btn().click()
#         self.page.map_icon().click()
#         #Megjelenik-e a cím, ha rákattint a helyzetjelző ikonra:
#         assert TESTDATA['address'] in self.page.address()
#         self.page.contact_name().send_keys(TESTDATA['contact_name'])
#         self.page.contact_email().send_keys(TESTDATA['contact_email'])
#         self.page.contact_field().send_keys(TESTDATA['contact_field'])
#         self.page.contact_send_btm().click()
#         #Sikerességet igazoló üzenet megjelenése:
#         assert self.page.contact_msg_succ() == TESTDATA['contact_msg_succ']
#         #Egyezik, megjelenik az adatbázisban a beírt név, email cím, üzenet szövege:
#         assert TESTDATA['contact_name'] and TESTDATA['contact_email'] and TESTDATA['contact_field'] in self.page.last_msg()
#         self.page.contact_send_btn().click()
#
#     def test_emailback(self):
#         self.page.new_tab_email()


