import random, string


class DataPage:
	def __init__(self):
		self.english_chars_all ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		self.english_chars = 'abcdefghijklmnopqrstuvwxyz'
		self.russian_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
		self.chinese_chars = '的一是不了人我在有他这为之大来以个中上们'
		self.special_chars = r'|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

	def random_ls(self):
		return random.randint(100000000000, 999999999999)

	def english_string(self, symbols=16):
		return ''.join(random.choice(self.english_chars) for _ in range(symbols))

	def english_all_string(self, symbols=16):
		return ''.join(random.choice(self.english_chars_all) for _ in range(symbols))

	def russian_string(self, symbols=16):
		return ''.join(random.choice(self.russian_chars) for _ in range(symbols))

	def chinese_string(self, symbols=16):
		return ''.join(random.choice(self.chinese_chars) for _ in range(symbols))

	def special_string(self, symbols=16):
		return ''.join(random.choice(self.special_chars) for _ in range(symbols))

	def email(self):
		new_email = list(f'{self.english_string(12)}@{self.english_string(8)}')
		new_email[-4] = '.'
		return ''.join(new_email)

	def phone(self):
		return '+7'+str(random.randint(1000000000, 9999999999))

	def password(self):
		return self.english_all_string(12)+self.special_string(4)

	def valid_users(self):
		return [(self.english_all_string(), self.password()),
		        (self.russian_string(), self.password()),
		        (self.chinese_string(), self.password()),
		        (self.special_string(), self.password())]

	def valid_phone_users(self):
		return [(self.phone(), self.password())]

	def valid_email_users(self):
		return [(self.email(), self.password())]

	def valid_login_users(self):
		return [(self.english_string(), self.password())]

	def valid_ls_users(self):
		return [(self. random_ls(), self.password())]

	def valid_user_names(self):
		return [self.russian_string() for _ in range(1)]

	def valid_email_and_phone(self):
		list = []
		for _ in range(1):
			list.append(self.email())
			list.append(self.phone())
		return list

	def valid_passwords(self):
		return [self.password() for _ in range(1)]

	def valid_reg_users(self):
		return [(self.russian_string(), self.email(), self.password())]

	def invalid_user_names(self):
		return [self.english_string(), self.special_string()]

	def invalid_email_and_phone(self):
		list = []
		for _ in range(1):
			list.append(self.english_string())
			list.append(self.random_ls())
		return list

	def invalid_passwords(self):
		return [self.english_all_string(6), self.russian_string(), self.english_string()]