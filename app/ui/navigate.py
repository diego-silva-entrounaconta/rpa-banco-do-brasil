"""Imports"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def navigate_to_proposal_printing(driver: WebDriver):
    """Function navigate to proposal printing"""
    table_item_product = driver.find_element(by=By.ID, value="idtab3_lbl")
    table_item_product.click()

    link = driver.find_element(by=By.ID, value="j_id173")
    link.click()


def navigate_to_daily_movement(driver: WebDriver):
    """Function navigate to daily moment"""
    driver.get(
        "https://www47.bb.com.br/maisbb/produtos/emprestimo/movimentodiarioproducao.seam"
    )
