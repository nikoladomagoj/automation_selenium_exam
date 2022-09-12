from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
#time.sleep(5)