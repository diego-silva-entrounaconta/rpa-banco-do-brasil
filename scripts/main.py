from selenium import webdriver
from time import sleep
from actions import login, navigate, search, click


def main():
    url = "https://www47.bb.com.br/maisbb/gcs/statics/login/login.bb#/j"

    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=opt)
    driver.get(url)

    print("Bem vindo a ENC!")

    sleep(5)

    driver.implicitly_wait(5)

    # accessing the bank of brazil website
    login.make_login(driver)

    driver.implicitly_wait(5)

    # navigating to the proposal print tab
    navigate.navigate_to_proposal_printing(driver)

    search.search_proposal(driver)

    click.generate_proposal(driver)

    input("Pressione Enter para encerrar o programa e fechar o navegador...")
    driver.quit()


if __name__ == "__main__":
    main()
