import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver(chrome_driver_path):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(chrome_driver_path)
    try:
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
        raise

def run_script():
    # Path to the ChromeDriver
    chrome_driver_path = "/Users/mohammademan/chromedriver-mac-arm64/chromedriver"

    # Check if the ChromeDriver path is correct
    import os
    if not os.path.exists(chrome_driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}. Please check the path and try again.")

    # Set up the WebDriver
    driver = setup_driver(chrome_driver_path)

    # Open a webpage
    driver.get("https://www.example.com")

    try:
        # Wait for an element to be present and interact with it
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Example Domain']"))
        )
        print("Element found:", element.text)

        # Perform more interactions as needed
        time.sleep(2)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        driver.quit()

# Run the script
if __name__ == "__main__":
    run_script()