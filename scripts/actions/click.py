from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from time import sleep


def generate_proposal(driver: WebDriver):
    wait = WebDriverWait(driver, timeout=10)

    # inputs_radio = driver.find_elements(by=By.NAME, value="proposta")
    inputs_radio = wait.until(
        EC.presence_of_all_elements_located((By.NAME, "proposta"))
    )

    for i, ipt in enumerate(inputs_radio):
        inputs_radio = wait.until(
            EC.presence_of_all_elements_located((By.NAME, "proposta"))
        )
        ipt = inputs_radio[i]
        ipt.click()
        btn_generate_proposal = driver.find_element(
            by=By.ID, value="form1:j_id434:botaoGerarProposta"
        )
        btn_generate_proposal.click()

        btn_download = driver.find_element(by=By.NAME, value="j_id1")
        btn_download.click()

        sleep(2)
        """
        btn_save = driver.find_element(by=By.CLASS_NAME, value="action-button")
        btn_save.click()
        """

        action = ActionChains(driver)
        action.key_down(Keys.ENTER)

        sleep(2)
        driver.back()
        sleep(3)
