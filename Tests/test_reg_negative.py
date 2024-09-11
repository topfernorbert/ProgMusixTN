from ProgMusix.configs.config import get_preconfigured_chrome_driver
from ProgMusix.page_model import ProgMusix
from ProgMusix.configs.testdata import TESTDATA


class TestProgmusix:
    def setup_method(self):
        page = ProgMusix(get_preconfigured_chrome_driver())
        self.page = page
        page.open()

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

    # Csak a username kitöltése helytelen:
    def test_reg_invalid_username(self):
        self.page.registration_invalid_name()
        assert not self.page.register_btn().is_enabled()

    # Csak az email cím formátuma helytelen:
    def test_reg_invalid_email(self):
        self.page.registration_invalid_email()
        assert not self.page.register_btn().is_enabled()

    # Csak a jelszó formátuma helytelen:
    def test_reg_invalid_password(self):
        self.page.registration_invalid_password()
        assert not self.page.register_btn().is_enabled()

    # Eltérő jelszómegerősítés:

    def test_reg_dif_password(self):
        self.page.registration_dif_password()
        assert not self.page.register_btn().is_enabled()