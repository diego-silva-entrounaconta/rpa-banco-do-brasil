from selenium import webdriver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from actions import login, navigate


def main():
    driver = webdriver.Chrome()
    driver.get("https://www47.bb.com.br/maisbb/gcs/statics/login/login.bb#/j")

    print("Bem vindo a ENC!")

    sleep(5)

    # accessing the bank of brazil website
    login.make_login(driver)

    # navigating to the proposal print tab
    navigate.navigate_to_proposal_printing(driver)

    # select = driver.find_element(by=By.NAME, value="form1:j_id377")
    # select.click()

    # action = ActionChains(driver)
    # action.key_down(Keys.ARROW_DOWN).perform()
    # action.key_down(Keys.ARROW_DOWN).perform()
    # action.key_down(Keys.ENTER).perform()

    input("Pressione Enter para encerrar o programa e fechar o navegador...")
    driver.quit()


if __name__ == "__main__":
    main()
