from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Paso 2:
# Permite personalizar el comportamiento del navegador que Selenium controla.
# options = webdriver.ChromeOptions()
# Esta configuración evita que el navegador se cierre automáticamente al final del script. Ello tiene que ver también "detach"
# options.add_experimental_option("detach", True)

# Paso 1: Abrir la web requerida
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://duolingo.com")

# Paso 3:
# Buscar la opcion para iniciar sesión y darle click
link = browser.find_element(
    By.XPATH, "//span[text()='I ALREADY HAVE AN ACCOUNT']")
link.click()

# Paso 4:
# Seleccionar las cajas de usuario y clave
user_input = browser.find_element(By.ID, "web-ui1")
pass_input = browser.find_element(By.ID, "web-ui2")

# Paso 5:
# Ingreso usuario y clave
user_input.send_keys(os.environ.get("duo_user").strip())
pass_input.send_keys(os.environ.get("duo_pass").strip())

# Paso 6:
pass_input.send_keys(Keys.RETURN)"
# Paso 7:
# Ingresar al botón perfil para validar el usuario
# pre_profile = browser.find_element(By.XPATH, "//span[text()='Perfil']")
# pre_profile.click()

pre_profile = browser.find_element(
    By.XPATH, "//span[@class='_1AZJt' and text()='Perfil']")
pre_profile.click()


# Paso 8:
# Validar el profile
profile = browser.find_element(By.CSS_SELECTOR, "div.fs-exclude._1Fdxc")


# Paso 9
# Mostrar al usuario
label = profile.get_attribute("innerHTML")


# Paso 10
# Validar si es el usuario correcto
assert os.environ.get("duo_web_user").strip() in label
browser.implicitly_wait(5)
browser.quit()
