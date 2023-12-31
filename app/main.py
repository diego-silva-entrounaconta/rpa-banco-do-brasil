import dotenv
import os
from time import sleep
from app.workflow import steps
from configuration import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables from .env file
dotenv.load_dotenv()

# Access environment variables
url = os.getenv("URL")


def main():
    print("Starting...")

    # Add arguments to browser options
    opt = Options()
    for index, args in enumerate(settings.arguments):
        opt.add_argument(args)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opt)
    driver.get(url)

    sleep(5)

    driver.implicitly_wait(5)

    print("Step one")
    # Calling step by step
    steps.step_one(driver)

    print("Step two")
    sleep(1)
    steps.step_two(driver)

    print("Step three")
    sleep(1)
    steps.step_three(driver)

    print("Step four")
    sleep(1)
    steps.step_four(driver)

    print("Step five")
    sleep(1)
    steps.step_five()

    print("Finishing...")

    sleep(1.5)
    driver.quit()


if __name__ == "__main__":
    main()

