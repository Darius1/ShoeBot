from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

path="C:\Python27\selenium\geckodriver"
driver=webdriver.Firefox(path)
print(os.path)
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()