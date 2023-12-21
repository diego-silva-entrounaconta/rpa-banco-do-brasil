from selenium.webdriver.chrome.webdriver import WebDriver
from ui import login, navigate
from actions import search, click, email


def step_one(driver: WebDriver):
    # accessing the bank of brazil website
    login.make_login(driver)

    driver.implicitly_wait(5)

    # navigating to the proposal print tab
    navigate.navigate_to_proposal_printing(driver)


def step_two(driver: WebDriver):
    search.search_proposal(driver)

    click.generate_proposal(driver)


def step_three(driver: WebDriver):
    navigate.navigate_to_daily_movement(driver)

    search.search_daily_moviment(driver)

def step_four(driver: WebDriver):
    
    # email.send_email()
