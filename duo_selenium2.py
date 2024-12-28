from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

browser = webdriver.Chrome()
browser.get("https://duolingo.com")

link = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[text()='I ALREADY HAVE AN ACCOUNT']"))
)
link.click()

user_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "web-ui1"))
)
pass_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "web-ui2"))
)

user_input.send_keys(os.environ.get("duo_user").strip())
pass_input.send_keys(os.environ.get("duo_pass").strip())


pass_input.send_keys(Keys.RETURN)


pre_profile = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[@class='_1AZJt' and text()='Perfil']"))
)
pre_profile.click()

profile = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.fs-exclude._1Fdxc"))
)


label = profile.get_attribute("innerHTML")
print(label)


assert os.environ.get("duo_web_user").strip() in label
browser.implicitly_wait(5)
browser.quit()
