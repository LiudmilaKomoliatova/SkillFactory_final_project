from .base_page import BasePage
from .locators import AuthLocators


class AuthPage(BasePage):
	# oткрыте формы авторизации
	def open_authorization_form(self):
		assert self.is_element_present(AuthLocators.AUTH_HEADING)
		assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
			"url do not match"

	# расположения логотипа и слогана
	def location_of_logo_and_slogan(self):
		assert self.is_element_present(AuthLocators.AUTH_LOGO), "element LOGO not found"
		assert self.is_element_present(AuthLocators.AUTH_SLOGAN), "element SLOGAN not found"

	# проверка типа аутентификации по умолчанию
	def default_authentication_type(self):
		assert self.is_element_present(AuthLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_PHONE), \
			"element PLACEHOLDER_TELEPHONE not found"

	# проверка типов аутентификации
	def location_of_menu(self):
		self.find_element(AuthLocators.AUTH_TAB_PHONE).click()
		element = self.find_element(AuthLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_PHONE)
		assert "Мобильный телефон" in element.text, "element PLACEHOLDER not found"
		self.find_element(AuthLocators.AUTH_TAB_EMAIL).click()
		element = self.find_element(AuthLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_EMAIL)
		assert "Электронная почта" in element.text, "element PLACEHOLDER not found"
		self.find_element(AuthLocators.AUTH_TAB_LOGIN).click()
		element = self.find_element(AuthLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_LOGIN)
		assert "Логин" in element.text, "element PLACEHOLDER not found"
		self.find_element(AuthLocators.AUTH_TAB_LS).click()
		element = self.find_element(AuthLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_LS)
		assert "Лицевой счёт" in element.text, "element PLACEHOLDER not found"

	# сценарий авторизации по телефону и паролю
	def phone_authorization(self, phone, passw, positive=True):
		self.find_element(AuthLocators.AUTH_TAB_PHONE).click()
		self.find_element(AuthLocators.AUTH_USERNAME_INPUT).send_keys(phone)
		self.find_element(AuthLocators.AUTH_PASSWORD_INPUT).send_keys(passw)
		self.find_element(AuthLocators.AUTH_ENTER_BUTTON).click()
		if positive:
			element = self.find_element(AuthLocators.AUTH_OUT_BUTTON)
			assert "Выйти" in element.text, "authorization failed"
		else:
			element = self.find_element(AuthLocators.AUTH_ERROR)
			assert "Неверный логин или пароль" in element.text, "authorization failed message not found"

	# сценарий авторизации по почте и паролю
	def email_authorization(self, email, passw, positive=True):
		self.find_element(AuthLocators.AUTH_TAB_EMAIL).click()
		self.find_element(AuthLocators.AUTH_USERNAME_INPUT).send_keys(email)
		self.find_element(AuthLocators.AUTH_PASSWORD_INPUT).send_keys(passw)
		self.find_element(AuthLocators.AUTH_ENTER_BUTTON).click()
		if positive:
			element = self.find_element(AuthLocators.AUTH_OUT_BUTTON)
			assert "Выйти" in element.text, "authorization failed"
		else:
			element = self.find_element(AuthLocators.AUTH_ERROR)
			assert "Неверный логин или пароль" in element.text, "authorization failed message not found"

	# сценарий авторизации по логину и паролю
	def login_authorization(self, login, passw, positive=True):
		self.find_element(AuthLocators.AUTH_TAB_LOGIN).click()
		self.find_element(AuthLocators.AUTH_USERNAME_INPUT).send_keys(login)
		self.find_element(AuthLocators.AUTH_PASSWORD_INPUT).send_keys(passw)
		self.find_element(AuthLocators.AUTH_ENTER_BUTTON).click()
		if positive:
			element = self.find_element(AuthLocators.AUTH_OUT_BUTTON)
			assert "Выйти" in element.text, "authorization failed"
		else:
			element = self.find_element(AuthLocators.AUTH_ERROR)
			assert "Неверный логин или пароль" in element.text, "authorization failed message not found"

	# сценарий авторизации по лицевому счёт и паролю
	def ls_authorization(self, ls, passw, positive=True):
		self.find_element(AuthLocators.AUTH_TAB_LS).click()
		self.find_element(AuthLocators.AUTH_USERNAME_INPUT).send_keys(ls)
		self.find_element(AuthLocators.AUTH_PASSWORD_INPUT).send_keys(passw)
		self.find_element(AuthLocators.AUTH_ENTER_BUTTON).click()
		if positive:
			element = self.find_element(AuthLocators.AUTH_OUT_BUTTON)
			assert "Выйти" in element.text, "authorization failed"
		else:
			element = self.find_element(AuthLocators.AUTH_ERROR)
			assert "Неверный логин или пароль" in element.text, "authorization failed message not found"
