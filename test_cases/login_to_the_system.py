import os
import unittest
import time
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def testlogin_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user05@getnada.com')
        user_password = LoginPage(self.driver)
        user_password.type_in_password('Test-1234')
        user_login.sign_in()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
