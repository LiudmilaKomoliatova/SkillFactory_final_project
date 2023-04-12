import pytest
from settings import *
from pages.reg_page import RegPage
from pages.data_page import DataPage


class TestRegPage():
	def test_RR001_open_registration_form(self, browser):
		reg_page = RegPage(browser, URL_PAGE)
		reg_page.open_registration_form()

	@pytest.mark.parametrize('valid_name', DataPage().valid_user_names())
	def test_RR002_user_name_field_validation(self, browser, valid_name):
		reg_page = RegPage(browser, URL_PAGE)
		reg_page.user_name_field_validation(valid_name)

	@pytest.mark.parametrize('user_data', DataPage().valid_email_and_phone())
	def test_RR003_email_and_phone_field_validation(self, browser, user_data):
		reg_page = RegPage(browser, URL_PAGE)
		reg_page.email_and_phone_field_validation(user_data)

	@pytest.mark.parametrize('passw', DataPage().valid_passwords())
	def test_RR004_password_field_validation(self, browser, passw):
		reg_page = RegPage(browser, URL_PAGE)
		reg_page.password_field_validation(passw)

	@pytest.mark.parametrize('data', DataPage().valid_reg_users())
	def test_RR005_registration_check(self, browser, data):
		reg_page = RegPage(browser, URL_PAGE)
		reg_page.registration_check(data)