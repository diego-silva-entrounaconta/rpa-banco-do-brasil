from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from app.ui import login, navigate
from app.actions import search, click, get_and_set, email
from app.utils import get_data
from app.configuration import data

date_yesterday = get_data.get_date_yesterday()


def step_one(driver):
    # Accessing the bank of brazil website
    login.make_login(driver)

    driver.implicitly_wait(5)

    # Navigating the daily movement of products and searching for proposals
    navigate.navigate_to_daily_movement(driver)

    search.search_daily_moviment(driver, date_yesterday)


def step_two(driver: WebDriver):
    # Creating and storing the first data
    get_and_set.get_and_set_data_by_consult(driver)


def step_three(driver: WebDriver):
    # Navigating to the proposal print tab
    navigate.navigate_to_proposal_printing(driver)


def step_four(driver: WebDriver):
    # Searching for the latest data to create excel
    for i, dt in enumerate(data.dados):
        search.search_proposal(driver, dt[5])
        sleep(1)

        click.generate_proposal(driver, dt)


def step_five():
    # Create Excek and Send email
    email.send_email()
