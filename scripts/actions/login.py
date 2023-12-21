import dotenv
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

# Carrega as variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

# Acesse as variáveis de ambiente
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


def make_login(driver: WebDriver):
    input_login = driver.find_element(by=By.NAME, value="chave")
    input_password = driver.find_element(by=By.NAME, value="senha")

    driver.implicitly_wait(2)
    input_login.send_keys(login)
    input_password.send_keys(password)

    action = ActionChains(driver)
    action.key_down(Keys.ENTER).perform()

    btn_close_modal = driver.find_element(
        by=By.XPATH, value='//*[@id="j_id364:form1:pnlContentDiv"]/div/a'
    )
    btn_close_modal.click()
