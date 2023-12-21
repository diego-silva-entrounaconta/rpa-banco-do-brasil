import dotenv
import os
from selenium import webdriver
from time import sleep
from workflow import steps

# Load environment variables from .env file
dotenv.load_dotenv()

# Access environment variables
url = os.getenv("URL")


def main():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=opt)
    driver.get(url)

    sleep(5)

    driver.implicitly_wait(5)

    steps.step_one(driver)

    # sleep(1)
    # steps.step_two(driver)

    sleep(1)
    steps.step_three(driver)

    input("não fechar")
    driver.quit()


if __name__ == "__main__":
    main()
