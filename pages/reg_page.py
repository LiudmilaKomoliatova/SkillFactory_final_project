from .base_page import BasePage
from .locators import RegLocators


class RegPage(BasePage):
	def open_registration_form(self):
		self.find_element(RegLocators.REG_LINK).click()
		assert self.is_element_present(RegLocators.REG_HEADING), "element not found"

	def user_name_field_validation(self, user_name, positive=True):
		self.find_element(RegLocators.REG_LINK).click()
		assert self.is_element_present(RegLocators.REG_FIRST_NAME_INPUT), "element FIRST_NAME_INPUT not found"
		assert self.is_element_present(RegLocators.REG_LAST_NAME_INPUT), "element LAST_NAME_INPUT not found"
		self.find_element(RegLocators.REG_FIRST_NAME_INPUT).send_keys(user_name)
		self.find_element(RegLocators.REG_HEADING).click()
		self.find_element(RegLocators.REG_LAST_NAME_INPUT).send_keys(user_name)
		self.find_element(RegLocators.REG_HEADING).click()
		if positive:
			assert self.is_not_element_present(RegLocators.REG_ERROR_INPUT), "element found"
		else:
			assert self.is_element_present(RegLocators.REG_ERROR_INPUT), "element not found"

	def email_and_phone_field_validation(self, user_data, positive=True):
		self.find_element(RegLocators.REG_LINK).click()
		assert self.is_element_present(RegLocators.REG_EMAIL_PHONE_INPUT), "element EMAIL_PHONE_INPUT not found"
		self.find_element(RegLocators.REG_EMAIL_PHONE_INPUT).send_keys(user_data)
		self.find_element(RegLocators.REG_HEADING).click()
		if positive:
			assert self.is_not_element_present(RegLocators.REG_ERROR_INPUT), "element found"
		else:
			assert self.is_element_present(RegLocators.REG_ERROR_INPUT), "element not found"

	def password_field_validation(self, passw, positive=True):
		self.find_element(RegLocators.REG_LINK).click()
		assert self.is_element_present(RegLocators.REG_PASSWORD_INPUT), "element PASSWORD_INPUT not found"
		assert self.is_element_present(RegLocators.REG_PASSWORD_CONFIRM_INPUT), "element PASSWORD_INPUT2 not found"
		self.find_element(RegLocators.REG_PASSWORD_INPUT).send_keys(passw)
		self.find_element(RegLocators.REG_HEADING).click()
		self.find_element(RegLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(passw)
		self.find_element(RegLocators.REG_HEADING).click()
		if positive:
			assert self.is_not_element_present(RegLocators.REG_ERROR_INPUT), "element found"
		else:
			assert self.is_element_present(RegLocators.REG_ERROR_INPUT), "element not found"

	def registration_check(self, data, positive=True):
		self.find_element(RegLocators.REG_LINK).click()
		self.find_element(RegLocators.REG_FIRST_NAME_INPUT).send_keys(data[0])
		self.find_element(RegLocators.REG_LAST_NAME_INPUT).send_keys(data[0])
		self.find_element(RegLocators.REG_EMAIL_PHONE_INPUT).send_keys(data[1])
		self.find_element(RegLocators.REG_PASSWORD_INPUT).send_keys(data[2])
		self.find_element(RegLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(data[2])
		self.find_element(RegLocators.REG_ENTER_BUTTON).click()
		if positive:
			assert self.is_not_element_present(RegLocators.EMAIL_CONF_HEADING), "element found"
		else:
			assert self.is_element_present(RegLocators.EMAIL_CONF_HEADING), "element not found"
