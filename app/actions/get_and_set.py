from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from configuration import data
from time import sleep
from typing import List


def get_and_set_data_by_proposal(driver: WebDriver, dt: List[str]):
    # Função responsavel por buscar os dados e setar eles

    cpf = driver.find_element(by=By.ID, value="cpf").text
    client_name = driver.find_element(by=By.ID, value="nome").text
    agreement = driver.find_element(by=By.ID, value="nomeConvenio").text
    number = driver.find_element(by=By.ID, value="numConvenio").text
    agreement_and_number = f"{agreement} - {number}"

    table = driver.find_elements(by=By.CLASS_NAME, value="linha2")
    data_dict = {}
    for i, r in enumerate(table):
        if i % 2 == 0:
            key = r.text
        else:
            value = r.text
            data_dict[key] = value

    proposal_number = data_dict["Número da proposta:"]
    credit_line = data_dict["Linha de crédito:"]
    rate = data_dict["Taxa Mensal de Juros (%):"]
    installment_value = data_dict["Valor Parcela"]
    gross_value = data_dict["Valor Total do Empréstimo:"]
    net_value = data_dict["Valor solicitado"]

    data_list = [
        cpf,
        client_name,
        credit_line,
        agreement_and_number,
        rate,
        installment_value,
        gross_value,
        net_value,
    ]

    type_of_proposal = ""

    if dt[0] == proposal_number:
        if dt[3] == "0,00" and credit_line == "BB RENOVAÇÃO CONSIGNAÇÃO":
            type_of_proposal = "REFIN S/ TROCO"
        elif dt[3] != "0,00":
            type_of_proposal = "REFIN C/ TROCO"
        else:
            type_of_proposal = "NOVO"

        for i, item in enumerate(data_list):
            dt.append(item)

        dt.append(type_of_proposal)

    return


def get_and_set_data_by_consult(driver: WebDriver):
    row = driver.find_elements(by=By.CLASS_NAME, value="rich-table-row")

    for i, r in enumerate(row):
        situation_bank = driver.find_element(
            by=By.ID, value=f"form1:tableProducaoSelecionada:{i}:j_id542"
        ).text

        if situation_bank == "Contratada":
            proposal_number = driver.find_element(
                by=By.ID, value=f"form1:tableProducaoSelecionada:{i}:j_id521"
            ).text
            term = driver.find_element(
                by=By.ID, value=f"form1:tableProducaoSelecionada:{i}:j_id530"
            ).text
            change = driver.find_element(
                by=By.ID, value=f"form1:tableProducaoSelecionada:{i}:j_id539"
            ).text
            typing_user = driver.find_element(
                by=By.ID, value=f"form1:tableProducaoSelecionada:{i}:j_id551"
            ).text

            data_list = [
                proposal_number,
                situation_bank,
                term,
                change,
                typing_user,
            ]

            driver.find_element(
                by=By.ID, value=f"form1:tableProducaoSelecionada:{i}:j_id554"
            ).click()

            date_typing = driver.find_element(
                by=By.ID, value="formdetalhehistorico:tbldetalhehistorico:0:j_id369"
            ).text
            hiring_date = driver.find_element(
                by=By.ID, value="formdetalhehistorico:tbldetalhehistorico:1:j_id369"
            ).text

            data_list.append(date_typing)
            data_list.append(hiring_date)
            data.dados.append(data_list)

            sleep(1)
            driver.back()
            sleep(1)

    return
