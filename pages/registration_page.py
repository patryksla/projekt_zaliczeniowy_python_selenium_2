from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from selenium.webdriver.common.keys import Keys



class RegistrationPage(BasePage):

    def _verify_page(self):
        print("Weryfikacja RegistartionPage")
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))

    def fill_name(self, name):
        element = self.driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        element.send_keys(name)

    def fill_surname(self, surname):
        element = self.driver.find_element(*RegistrationPageLocators.SURNAME_INPUT)
        element.send_keys(surname)

    def choose_nationality(self):
        element = self.driver.find_element(*RegistrationPageLocators.NATIONALITY_INPUT)
        element.click()
        self.driver.find_element(*RegistrationPageLocators.NATIONALITY_CHOOSE).click()

    def voivodeship(self):
        wait = WebDriverWait(self.driver, 60)
        registration_page_element = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.VOIVODESHIP_INPUT))
        registration_page_element.click()
        element = self.driver.find_element(*RegistrationPageLocators.VOIVODESHIP_INPUT)
        element.click()
        wait = WebDriverWait(self.driver, 60)
        registration_page_element = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.VOIVODESHIP_CHOOSE))
        registration_page_element.click()
        self.driver.find_element(*RegistrationPageLocators.VOIVODESHIP_CHOOSE).click()

    def fill_street(self, street):
        element = self.driver.find_element(*RegistrationPageLocators.STREET_INPUT)
        element.send_keys(street)

    def fill_building_number(self, building_number):
        element = self.driver.find_element(*RegistrationPageLocators.BUILDING_NUMBER_INPUT)
        element.send_keys(building_number)

    def fill_postal_code(self, postal_code):
        element = self.driver.find_element(*RegistrationPageLocators.POSTAL_CODE_INPUT)
        element.send_keys(postal_code)

    def fill_city(self, city):
        element = self.driver.find_element(*RegistrationPageLocators.CITY_INPUT)
        element.send_keys(city)

    def fill_phone_number(self, phone_number):
        element = self.driver.find_element(*RegistrationPageLocators.PHONE_NUMBER_INPUT)
        element.send_keys(phone_number)

    def fill_email(self, email):
        element = self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        element.send_keys(email)

    def fill_password(self, password):
        element = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        element.send_keys(password)

    def fill_password_confirmation(self, password_confirmation):
        element = self.driver.find_element(*RegistrationPageLocators.PASSWORD_CONFIRMATION_INPUT)
        element.send_keys(password_confirmation)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)


    def accept_agreement(self):
        self.driver.implicitly_wait(60)
        element = self.driver.find_element(*RegistrationPageLocators.ACCEPT_AGREEMENT1)
        element.click()

    def accept_rodo(self):
        self.driver.implicitly_wait(60)
        element = self.driver.find_element(*RegistrationPageLocators.ACCEPT_RODO)
        element.click()

    def create_account(self):
        self.driver.implicitly_wait(60)
        element = self.driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT)
        element.click()
