from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from configuration import data


def get_and_set_data_by_proposal(driver: WebDriver):
    cpf = driver.find_element(by=By.ID, value="cpf").text
    client_name = driver.find_element(by=By.ID, value="nome").text
    agreement = driver.find_element(by=By.ID, value="nomeConvenio").text
    number = driver.find_element(by=By.ID, value="numConvenio").text
    agreement_and_number = f"{agreement} - {number}"
    typing_user = driver.find_element(by=By.ID, value="chaveOperador").text

    # other - date_typing = driver.find_element(by=By.ID, value="cpf")
    # other - situation company_bank = driver.find_element(by=By.ID, value="cpf")
    # other - type_of_proposal = driver.find_element(by=By.ID, value="cpf")

    table = driver.find_elements(by=By.CLASS_NAME, value="linha2")
    data_dict = {}
    for i, r in enumerate(table):
        if i % 2 == 0:
            key = r.text
        else:
            value = r.text
            data_dict[key] = value

    credit_line = data_dict["Linha de crédito:"]
    proposal_number = data_dict["Número da proposta:"]
    rate = data_dict["Taxa Mensal de Juros (%):"]
    term = data_dict["Prazo em Meses:"]
    installment_value = data_dict["Valor Parcela"]
    gross_value = data_dict["Valor Total do Empréstimo:"]
    net_value = data_dict["Valor solicitado"]

    data_list = [
        cpf,
        client_name,
        credit_line,
        proposal_number,
        agreement_and_number,
        rate,
        term,
        installment_value,
        gross_value,
        net_value,
        typing_user,
    ]

    data.dados.append(data_list)

    return


def generate_proposal(driver: WebDriver):
    wait = WebDriverWait(driver, timeout=10)

    # inputs_radio = driver.find_elements(by=By.NAME, value="proposta")
    inputs_radio = wait.until(
        EC.presence_of_all_elements_located((By.NAME, "proposta"))
    )

    for i, ipt in enumerate(inputs_radio):
        inputs_radio = wait.until(
            EC.presence_of_all_elements_located((By.NAME, "proposta"))
        )
        ipt = inputs_radio[i]
        ipt.click()
        btn_generate_proposal = driver.find_element(
            by=By.ID, value="form1:j_id434:botaoGerarProposta"
        )
        btn_generate_proposal.click()
        sleep(1.5)

        get_and_set_data_by_proposal(driver)

        sleep(1.5)
        driver.back()
        sleep(1.5)

    return
