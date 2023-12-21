from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def search_proposal(driver: WebDriver):
    inputs_date = driver.find_elements(by=By.CLASS_NAME, value="rich-calendar-input")

    for ipt in inputs_date:
        ipt.send_keys("12/12/2023")

    btn_find_proposal = driver.find_element(
        by=By.ID, value="form1:j_id405:botaoconsultar"
    )

    btn_find_proposal.click()
