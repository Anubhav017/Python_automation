import sys
import os


def main():
    # Define the pytest command
    pytest_command = "pytest -v -s ./tests/pictorytests -k sanity --alluredir=./reports/allure-results --env dev"
    # pytest_command = "pytest -v -s ./tests/pictorytests -k Regression --alluredir=./reports/allure-results --env dev"

    # Check the operating system
    if sys.platform.startswith('win'):
        # If Windows, use the command to execute the pytest command in a new terminal
        os.system(pytest_command)
    else:
        # If Linux, execute the pytest command directly
        os.system(pytest_command)


if __name__ == "__main__":
    main()
