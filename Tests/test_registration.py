from ProgMusix.configs.config import get_preconfigured_chrome_driver
from ProgMusix.page_model import ProgMusix
from ProgMusix.configs.testdata import TESTDATA
import time

class TestProgmusix:
    def setup_method(self):
        page = ProgMusix(get_preconfigured_chrome_driver())
        self.page = page
        page.open()
        
    def test_regtest(self):
        self.page.registration()
        self.page.reg_user_data_send()
        assert self.page.register_btn().is_enabled()
        assert self.page.succesfull_msg() == TESTDATA['succesful_msg']
        assert TESTDATA['email_p'] and TESTDATA['username_p'] in self.page.last_user_sql()
        time.sleep(5)

    def test_reg_email(self):
        # Annak ellenőrzése, hogy megérkezik a visszaigazoló e-mail és tartalmazza a kattintható aktiváló linket
        self.page.reg_email()
        assert self.page.activate_link().is_displayed()
        self.page.activate_link().click()
