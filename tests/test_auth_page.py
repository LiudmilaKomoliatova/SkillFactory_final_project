import pytest
from settings import *
from pages.auth_page import AuthPage
from pages.data_page import DataPage


class TestAuthPage():
	def test_RA001_authorization_form_is_open(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.open_authorization_form()

	def test_RA002_location_of_logo_and_slogan(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.location_of_logo_and_slogan()

	def test_RA003_location_of_menu(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.location_of_menu()

	def test_RA004_default_authentication_type(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.default_authentication_type()

	def test_RA005_phone_authorization(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.phone_authorization(VALID_PHONE, VALID_PHONE_PASSWORD)

	def test_RA006_email_authorization(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.email_authorization(VALID_EMAIL, VALID_EMAIL_PASSWORD)

	def test_RA007_login_authorization(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.login_authorization(VALID_LOGIN, VALID_LOGIN_PASSWORD)

	def test_RA008_ls_authorization(self, browser):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.ls_authorization(VALID_LS, VALID_LS_PASSWORD)

	@pytest.mark.parametrize('phone_users', DataPage().valid_phone_users())
	def test_RA009_negative_phone_authorization(self, browser, phone_users):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.phone_authorization(phone_users[0], phone_users[1], positive=False)

	@pytest.mark.parametrize('email_users', DataPage().valid_email_users())
	def test_RA010_negative_email_authorization(self, browser, email_users):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.email_authorization(email_users[0], email_users[1], positive=False)

	@pytest.mark.parametrize('login_users', DataPage().valid_login_users())
	def test_RA011_negative_login_authorization(self, browser, login_users):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.login_authorization(login_users[0], login_users[1], positive=False)

	@pytest.mark.parametrize('ls_users', DataPage().valid_ls_users())
	def test_RA012_negative_ls_authorization(self, browser, ls_users):
		auth_page = AuthPage(browser, URL_PAGE)
		auth_page.ls_authorization(ls_users[0], ls_users[1], positive=False)
