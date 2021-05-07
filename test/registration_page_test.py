import unittest
from base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from time import sleep

valid_name = "Piotr"
valid_surname = "Nowak"
valid_street = "Szkolna"
valid_building_number = "8"
valid_postal_code = "00-100"
valid_city = "Warszawa"
valid_phone_number = "783546228"
invalid_email ="piotr2.com"
valid_password = "Qwerty123!"
valid_password_confirmation = "Qwerty123!"

class RegistrationPageTest(BaseTest):

    def setUp(self):
        print("setUp z RegistrationPageTest")
        super().setUp()

        hp = HomePage(self.driver)
        hp.click_close_newsletter_btn()
        hp.click_zaloguj_btn()

        lp = LoginPage(self.driver)
        lp.click_register_btn()

    def test_incorrect_email(self):
        rp = RegistrationPage(self.driver)
        rp.fill_name(valid_name)
        rp.fill_surname(valid_surname)
        rp.choose_nationality()
        rp.voivodeship()
        rp.fill_street(valid_street)
        rp.fill_building_number(valid_building_number)
        rp.fill_postal_code(valid_postal_code)
        rp.fill_city(valid_city)
        rp.fill_phone_number(valid_phone_number)
        rp.fill_email(invalid_email)
        rp.fill_password(valid_password)
        rp.fill_password_confirmation(valid_password_confirmation)
        rp.accept_agreement()
        rp.accept_rodo()
        rp.create_account()
        rp.verify_visible_errors(1, ["Podany adres email jest nieprawidłowy"])

sleep(20)

if __name__=="__main__":
    unittest.main(verbosity=2)