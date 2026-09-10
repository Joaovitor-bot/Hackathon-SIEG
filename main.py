from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://talkabit-z3eg.onrender.com/app/login")

campo = driver.find_element(By.NAME, "teamToken")
campo.send_keys("AVATAR-73STC")

campo = driver.find_element(By.NAME, "password")
campo.send_keys("talkabit")

campo.send_keys(Keys.ENTER)

if driver.find_elements(By.CLASS_NAME, "np-overlay"):
  botao = driver.find_element(
    By.XPATH,
    "//div[contains(@class, 'np-overlay')]//button"
  )

  botao.click()

input("Pressione [ENTER] no terminal para o Selenium continuar o script...")

driver.quit()