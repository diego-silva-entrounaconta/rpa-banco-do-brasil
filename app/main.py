import dotenv
import os
from selenium import webdriver
from time import sleep
from workflow import steps
from configuration import settings

# Load environment variables from .env file
dotenv.load_dotenv()

# Access environment variables
url = os.getenv("URL")


def main():

    # Add arguments to browser options
    opt = webdriver.ChromeOptions()
    for index, args in enumerate(settings.arguments):
        opt.add_argument(args)

    # Create the browser instance and open
    driver = webdriver.Chrome(options=opt)
    driver.get(url)

    sleep(5)

    driver.implicitly_wait(5)

    # Calling step by step
    steps.step_one(driver)

    sleep(1)
    steps.step_two(driver)

    sleep(1)
    steps.step_three(driver)

    sleep(1)
    steps.step_four(driver)

    sleep(1)
    steps.step_five()

    sleep(1.5)
    driver.quit()


if __name__ == "__main__":
    main()
