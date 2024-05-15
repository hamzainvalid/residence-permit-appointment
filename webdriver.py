from selenium import webdriver


def get_chrome_driver_version(chrome_driver_path):
    driver_path = chrome_driver_path
    try:
        # Initialize a Chrome WebDriver instance
        driver = webdriver.Chrome(executable_path=driver_path)

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
    else:
        print("Failed to retrieve Chrome WebDriver version.")
