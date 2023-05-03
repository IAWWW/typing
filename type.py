from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from time import sleep


class type:
	def __init__(self):
		self.fastype()
		return
	
	def fastype(self):
		self.driver = webdriver.Chrome()																					#open Chrome
		self.driver.get("https://10fastfingers.com/text/185154-BUDDHA-ACADEMY-TIKAMGARH-MP-CPCT-Admission-Open")																			#load mathtrainer.org
		sleep(2)
		for text in self.driver.find_elements_by_id('row1'):
			for word in self.driver.find_elements_by_xpath('//span'):
				print(word.text)
				words = word.text
				self.driver.find_element_by_xpath('//input[@class="form-control changed"]').send_keys(words)


type()
