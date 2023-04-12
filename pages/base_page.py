from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
	def __init__(self, browser, url, timeout=5):
		self.browser = browser
		self.url = url
		self.time = timeout
		self.browser.implicitly_wait(timeout)
		self.browser.get(self.url)

	def find_element(self, locator):
		return WebDriverWait(self.browser, self.time).until(EC.presence_of_element_located(locator),
													   message=f"Can't find element by locator {locator}")

	def is_element_present(self, locator):
		try:
			WebDriverWait(self.browser, self.time).until(EC.presence_of_element_located((locator)))
		except (NoSuchElementException):
			return False
		else:
			return True

	def is_not_element_present(self, locator):
		try:
			WebDriverWait(self.browser, self.time).until(EC.presence_of_element_located((locator)))
		except (TimeoutException):
			return True
		else:
			return True

	def scroll_down(self, offset=0):
		offset = offset if offset != 0 else 'document.body.scrollHeight'
		self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))

	def scroll_up(self, offset=0):
		offset = offset if offset != 0 else '-document.body.scrollHeight'
		self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))

