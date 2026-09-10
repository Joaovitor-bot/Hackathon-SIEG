from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


form = driver.find_element(
    By.XPATH,
    "//div[contains(@class, 'card')]//form"
  )
form.submit()

if driver.find_elements(By.CLASS_NAME, "np-overlay"):
  botao = driver.find_element(
    By.XPATH,
    "//div[contains(@class, 'np-overlay')]//button"
  )

  botao.click()

from selenium.webdriver.common.by import By


notas = []

try:
  wait = WebDriverWait(driver, 10)
  linhas = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "span.badge.aut")
    )
)

  print("try")


  # if linhas:

  #     for linha in linhas:

  #         status = linha.find_element(
  #             By.CSS_SELECTOR,
  #             ".badge"
  #         ).text.strip()

  #         if status != "Autorizada":
  #             continue

  #         numero = linha.find_element(
  #             By.CSS_SELECTOR,
  #             "td:nth-child(1)"
  #         ).text.strip()

  #         emitente = linha.find_element(
  #             By.CSS_SELECTOR,
  #             "td:nth-child(2)"
  #         ).text.strip()

  #         valor = linha.find_element(
  #             By.CSS_SELECTOR,
  #             "td:nth-child(5)"
  #         ).text.strip()

  #         url = linha.find_element(
  #             By.CSS_SELECTOR,
  #             "td:nth-child(6) a"
  #         ).get_attribute("href")

  #         notas.append({
  #             "numero": numero,
  #             "emitente": emitente,
  #             "valor": valor,
  #             "url": url
  #         })
except Exception as e:
  print(f"Erro ao encontrar linhas: {e}")
  linhas = []


print(linhas)
for elemento in linhas:
  pai = elemento.find_element(By.XPATH, "..")
  print(pai)
  
input("Faça a interação no navegador e pressione ENTER para continuar...")

driver.quit()