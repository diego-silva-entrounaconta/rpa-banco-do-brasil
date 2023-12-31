import dotenv
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables from .env file
dotenv.load_dotenv()

# Access environment variables
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


def make_login(driver: WebDriver):
    wait = WebDriverWait(driver, timeout=10)

    # Search for inputs
    input_login = driver.find_element(by=By.NAME, value="chave")
    input_password = driver.find_element(by=By.NAME, value="senha")

    # Wait for the inputs to be on screen and fill them in
    driver.implicitly_wait(2)
    input_login.send_keys(login)
    input_password.send_keys(password)

    # Press Enter
    action = ActionChains(driver)
    action.key_down(Keys.ENTER).perform()

    # Close alert
    btn_close_modal = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="j_id364:form1:pnlContentDiv"]/div/a')
        )
    )
    btn_close_modal.click()
