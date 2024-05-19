from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chrome_driver_version(chrome_driver_path):
    try:
        # Initialize the ChromeDriver service
        service = Service(chrome_driver_path)

        # Initialize a Chrome WebDriver instance with the service
        driver = webdriver.Chrome(service=service)

        # Get the Chrome WebDriver version
        version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

        # Close the WebDriver
        driver.quit()

        return version
    except Exception as e:
        print("Error:", e)
        return None

def webDriver(chrome_driver_path):
    chrome_driver_version = get_chrome_driver_version(chrome_driver_path)
    if chrome_driver_version:
        print("Chrome WebDriver version:", chrome_driver_version)
        return chrome_driver_version
    else:
        print("Failed to retrieve Chrome WebDriver version.")
