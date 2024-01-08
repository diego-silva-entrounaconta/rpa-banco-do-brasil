from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


def navigate_to_proposal_printing(driver: WebDriver):
    # Function redirects the page until the proposal is printed
    table_item_product = driver.find_element(by=By.ID, value="idtab3_lbl")
    table_item_product.click()

    link = driver.find_element(by=By.ID, value="j_id173")
    link.click()


def navigate_to_daily_movement(driver: WebDriver):
    # Funciton redirect the page for daily movement
    driver.get(
        "https://www47.bb.com.br/maisbb/produtos/emprestimo/movimentodiarioproducao.seam"
    )
