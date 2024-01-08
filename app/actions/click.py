from time import sleep
from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from . import get_and_set


def generate_proposal(driver: WebDriver, dt: List[str]):
    wait = WebDriverWait(driver, timeout=10)

    rows = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "rich-table-row"))
    )

    for i, ipt in enumerate(rows):
        proposal_number = driver.find_element(
            by=By.ID, value=f"form1:tblhistorico:{i}:j_id414"
        ).text

        if proposal_number == dt[0]:
            driver.find_element(
                by=By.ID, value=f"form1:tblhistorico:{i}:j_id412"
            ).click()

            driver.find_element(
                by=By.ID, value="form1:j_id434:botaoGerarProposta"
            ).click()
            sleep(1.5)

            try:
                driver.find_element(by=By.NAME, value="j_id1")
                get_and_set.get_and_set_data_by_proposal(driver, dt)
            except NoSuchElementException:
                dt.append("DADOS NÃO ENCONTRADOS")

            dt.pop(3)
            sleep(1.5)
            driver.back()
            sleep(1.5)
    return
