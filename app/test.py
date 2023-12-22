# from tabulate import tabulate
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException


# wait = WebDriverWait(driver, timeout=10)
# # driver.

# inputs = driver.find_elements(by=By.TAG_NAME, value="input")
# for index, ipt in enumerate(inputs):
#     if ipt.get_attribute("type") == "text":
#         ipt.send_keys("JG915011")
#     else:
#         ipt.send_keys("ENC02001")

# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "primary"))).click()
# # driver.find_element(by=By.CLASS_NAME, value="primary").click()

# sleep(3)

# div_search = driver.find_elements(by=By.TAG_NAME, value="input")
# print(len(div_search))

# try:
#     btn = div_search.find_element(
#         by=By.TAG_NAME,
#         value="bb-icon",
#     )

#     print(btn)
# except NoSuchElementException:
#     print("element not found")
