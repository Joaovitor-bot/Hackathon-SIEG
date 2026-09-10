from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def criar_driver():
    options = Options()

    # Caso queira executar sem abrir a janela do navegador:
    # options.add_argument("--headless")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver


def esperar_elemento(driver, by, valor, timeout=10):
    wait = WebDriverWait(driver, timeout)

    return wait.until(
        EC.presence_of_element_located((by, valor))
    )


def main():
    driver = criar_driver()

    try:
        # 1. Acessar página
        driver.get("https://www.google.com")

        # 2. Esperar elemento
        campo_pesquisa = esperar_elemento(
            driver,
            By.NAME,
            "q"
        )

        # 3. Interagir com elemento
        campo_pesquisa.send_keys("Selenium Python")

        # 4. Enviar formulário
        campo_pesquisa.submit()

        # 5. Esperar resultado
        WebDriverWait(driver, 10).until(
            EC.title_contains("Selenium")
        )

        print("Título:", driver.title)

    except Exception as erro:
        print(f"Erro durante a automação: {erro}")

    finally:
        # 6. Fechar navegador
        driver.quit()


if __name__ == "__main__":
    main()