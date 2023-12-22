from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def search_proposal(driver: WebDriver, data: str):
    inputs_date = driver.find_elements(by=By.CLASS_NAME, value="rich-calendar-input")

    for ipt in inputs_date:
        ipt.clear()
        ipt.send_keys(data)

    btn_find_proposal = driver.find_element(
        by=By.ID, value="form1:j_id405:botaoconsultar"
    )

    btn_find_proposal.click()


def search_daily_moviment(driver: WebDriver, data: str):
    select_element = driver.find_element(by=By.NAME, value="form1:j_id377")
    select = Select(select_element)

    select.select_by_value("2")

    inputs_date = driver.find_elements(by=By.CLASS_NAME, value="rich-calendar-input")

    for ipt in inputs_date:
        ipt.clear()
        ipt.send_keys(data)

    btn_consult = driver.find_element(by=By.ID, value="form1:j_id457:botaoConsultar")
    btn_consult.click()

    btn_details = driver.find_element(by=By.CLASS_NAME, value="rich-table-cell")

    children_btn_details = btn_details.find_element(
        by=By.XPATH, value='//*[@id="form1:tableProducao:0:j_id491"]/a'
    )
    children_btn_details.click()
