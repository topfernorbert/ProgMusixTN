from ProgMusix.configs.config import get_preconfigured_chrome_driver
from ProgMusix.page_model import ProgMusix
from ProgMusix.configs.testdata import TESTDATA

import time



class TestProgmusix:
    def setup_method(self):
        page = ProgMusix(get_preconfigured_chrome_driver())
        self.page = page
        page.open()

    def test_login_positive(self):
        self.page.login_method_p()
        # A belépéshez szükséges gomb engedélyezve van-e:
        assert self.page.login_btn().is_enabled()

    def test_change_admin(self):
        self.page.change_admin_sql()