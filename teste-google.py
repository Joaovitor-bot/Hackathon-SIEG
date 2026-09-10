from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

campo = driver.find_element(By.NAME, "q")
campo.send_keys("teste")
campo.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()