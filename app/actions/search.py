from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def search_proposal(driver: WebDriver, data: str):
    # Function that searches for proposals for printing

    # Search calendar entries
    inputs_date = driver.find_elements(by=By.CLASS_NAME, value="rich-calendar-input")

    # Fill in the inputs
    for ipt in inputs_date:
        ipt.clear()
        ipt.send_keys(data)

    # Search for the query button and press it
    btn_find_proposal = driver.find_element(
        by=By.ID, value="form1:j_id405:botaoconsultar"
    )

    btn_find_proposal.click()


def search_daily_moviment(driver: WebDriver, data: str):
    # Function responsible for searching for daily movements

    # Find the select and choose an option
    select_element = driver.find_element(by=By.NAME, value="form1:j_id377")
    select = Select(select_element)

    select.select_by_value("2")

    # Search calendar entries
    inputs_date = driver.find_elements(by=By.CLASS_NAME, value="rich-calendar-input")

    # Fill in the inputs
    for ipt in inputs_date:
        ipt.clear()
        ipt.send_keys(data)

    # Search for the query button and press it
    btn_consult = driver.find_element(by=By.ID, value="form1:j_id457:botaoConsultar")
    btn_consult.click()

    # Search for error message container
    try:
        erro_container = driver.find_element(by=By.CLASS_NAME, value="err_msg")

        # If the error exists, close the program
        if erro_container:
            print("No data found!")
            driver.quit()
    except Exception:
        # Find the details button and press it
        btn_details = driver.find_element(by=By.CLASS_NAME, value="rich-table-cell")
        children_btn_details = btn_details.find_element(
            by=By.XPATH, value='//*[@id="form1:tableProducao:0:j_id491"]/a'
        )
        children_btn_details.click()
