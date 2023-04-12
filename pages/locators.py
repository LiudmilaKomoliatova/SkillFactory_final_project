from selenium.webdriver.common.by import By

class AuthLocators:
	AUTH_HEADING = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
	AUTH_LOGO = (By.XPATH, "//section[@id='page-left']/*/div[@class='what-is-container__logo-container']/*")
	AUTH_SLOGAN = (By.XPATH,
				   "//section[@id='page-left']/*//p[contains(text(),'Персональный помощник в цифровом мире "
				   "Ростелекома')]")
	AUTH_USERNAME_INPUT_PLACEHOLDER_PHONE = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")
	AUTH_USERNAME_INPUT_PLACEHOLDER_EMAIL = (By.XPATH, "//span[contains(text(),'Электронная почта')]")
	AUTH_USERNAME_INPUT_PLACEHOLDER_LOGIN = (By.XPATH, "//span[contains(text(),'Логин')]")
	AUTH_USERNAME_INPUT_PLACEHOLDER_LS = (By.XPATH, "//span[contains(text(),'Лицевой счёт')]")
	AUTH_TAB_PHONE = (By.ID, "t-btn-tab-phone")
	AUTH_TAB_EMAIL = (By.ID, "t-btn-tab-mail")
	AUTH_TAB_LOGIN = (By.ID, "t-btn-tab-login")
	AUTH_TAB_LS = (By.ID, "t-btn-tab-ls")
	AUTH_USERNAME_INPUT = (By.ID, "username")
	AUTH_PASSWORD_INPUT = (By.ID, "password")
	AUTH_ENTER_BUTTON = (By.ID, "kc-login")
	AUTH_OUT_BUTTON = (By.XPATH, "//div[@id='logout-btn']")
	AUTH_ERROR = (By.ID, "form-error-message")

class RegLocators:
	REG_LINK = (By.ID, "kc-register")
	REG_HEADING = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
	REG_FIRST_NAME_INPUT = (By.XPATH, "//span[contains(text(),'Имя')]/preceding-sibling::input")
	REG_LAST_NAME_INPUT = (By.XPATH, "//span[contains(text(),'Фамилия')]/preceding-sibling::input")
	REG_EMAIL_PHONE_INPUT = (By.XPATH,
	                         "//span[contains(text(),'E-mail или мобильный телефон')]/preceding-sibling::input")
	REG_PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
	REG_PASSWORD_CONFIRM_INPUT = (By.XPATH, "//input[@id='password-confirm']")
	REG_ERROR_INPUT = (By.XPATH,
	                   "//span[@class='rt-input-container__meta rt-input-container__meta--error']")
	REG_ENTER_BUTTON = (
	By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn']")
	EMAIL_CONF_HEADING = (By.XPATH, "//h1[contains(text(),'Подтверждение email')]")
