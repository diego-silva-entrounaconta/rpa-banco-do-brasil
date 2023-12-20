from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# from time import sleep


def main():
    print("Bem vindo a ENC!")
    driver = webdriver.Chrome()
    driver.get("https://www47.bb.com.br/maisbb/gcs/statics/login/login.bb#/j")

    sleep(5)

    input_login = driver.find_element(by=By.NAME, value="chave")
    input_password = driver.find_element(by=By.NAME, value="senha")
    # button_search = driver.find_element(by=By.ID, value="search-icon-legacy")

    driver.implicitly_wait(2)
    input_login.send_keys("JG915011")
    input_password.send_keys("ENC02001")
    # button_search.click()

    action = ActionChains(driver)
    action.key_down(Keys.ENTER).perform()

    btn_close_modal = driver.find_element(
        by=By.XPATH, value='//*[@id="j_id364:form1:pnlContentDiv"]/div/a'
    )
    btn_close_modal.click()

    table_item_product = driver.find_element(by=By.ID, value="idtab3_lbl")
    table_item_product.click()

    link = driver.find_element(by=By.ID, value="j_id167")
    link.click()

    select = driver.find_element(by=By.NAME, value="form1:j_id377")
    select.click()

    action.key_down(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).perform()

    input("Pressione Enter para encerrar o programa e fechar o navegador...")
    driver.quit()


if __name__ == "__main__":
    main()
