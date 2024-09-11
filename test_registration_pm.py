from ProgMusix.configs.config import get_preconfigured_chrome_driver
from ProgMusix.page_model import ProgMusix
from ProgMusix.configs.testdata import TESTDATA
import pytest
import time

class TestProgmusix:
    def setup_method(self):
        page = ProgMusix(get_preconfigured_chrome_driver())
        self.page = page
        page.open()
        
    def test_regtest(self):
        self.page.registration()
        assert self.page.current_url() == "http://localhost:4200/registration"
        self.page.reg_user_data_send()
        assert self.page.register_btn().is_enabled()
        assert self.page.succesfull_msg() == TESTDATA['succesful_msg']
        assert TESTDATA['email_p'] and TESTDATA['username_p'] in self.page.last_user_sql()
        time.sleep(5)
