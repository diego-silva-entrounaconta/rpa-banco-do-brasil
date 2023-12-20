from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def navigate_to_proposal_printing(driver: WebDriver):
    table_item_product = driver.find_element(by=By.ID, value="idtab3_lbl")
    table_item_product.click()

    link = driver.find_element(by=By.ID, value="j_id167")
    link.click()
