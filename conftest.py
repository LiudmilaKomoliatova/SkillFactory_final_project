import pytest
from selenium import webdriver
from pages.data_page import DataPage


@pytest.fixture(scope="function")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	browser.maximize_window()
	yield browser
	print("\nquit browser..")
	browser.quit()

# @pytest.fixture(params=DataPage().valid_phone_users())
# def phone_users(request):
#     return request.param
