import winreg
import os
from webdriver import webDriver

def get_chrome_version():
    try:
        # Open the Windows registry key where Chrome's version is stored
        reg_path = r"Software\Google\Chrome\BLBeacon"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)

        # Read the version value
        version, _ = winreg.QueryValueEx(key, "version")
        return version
    except Exception as e:
        print("Error:", e)
        return None

def download_webdriver_notification():
    str(chrome_version)
    chrome_version_initaials = int(chrome_version[:3])
    if chrome_version_initaials == 115 or chrome_version_initaials > 115:
        print(f'The program could not find the correct webdriver in the provided locations. Please download the webdriver version: {chrome_version_initaials} using this link:'+'https://googlechromelabs.github.io/chrome-for-testing/')
    else:
        print(f'The program could not find the correct webdriver in the provided locations. Please download the webdriver version:{chrome_version_initaials} using this link:'+'https://chromedriver.chromium.org/downloads')


def find_chrome_webdriver():
    # Check common directories where the Chrome WebDriver might be located
    common_locations = [
        os.path.join(os.getenv('ProgramFiles'), 'Google', 'Chrome', 'Application', 'chromedriver.exe'),
        os.path.join(os.getenv('ProgramFiles(x86)'), 'Google', 'Chrome', 'Application', 'chromedriver.exe'),
        # Add more locations if necessary
    ]

    # Check if the WebDriver exists in any of the common locations
    for location in common_locations:
        if os.path.exists(location):
            print("Chrome WebDriver found at:", location)
            webDriver(location)
            return location

    webdriver_path = input('The program could not find the webdriver in the obvious locations. Please copy and paste the path of your webdriver if you already have one insalled otherwise type N/n')
    if webdriver_path == 'n' or webdriver_path == 'N':
        return None
    elif os.path.exists(webdriver_path):
        webDriver(webdriver_path)
        return webdriver_path
    else:
        return None


def webdriver_checker():
    okay_to_run = False
    if chrome_webdriver_path:
        print("Chrome WebDriver found at:", chrome_webdriver_path)
        str(chrome_version)
        str(chrome_webdriver_path)
        webdriver_version = webDriver(chrome_webdriver_path)
        print(webdriver_version)
        str(webdriver_version)
        if chrome_version and chrome_version[:3] == webdriver_version[:3]:
            okay_to_run = True
        else:
            if chrome_version:
                download_webdriver_notification()
            else:
                print("Failed to retrieve Chrome version. Please install google chrome on your operating system")
    else:
        print("Chrome WebDriver not found.")
        if chrome_version:
            print("Chrome version:", chrome_version)
            download_webdriver_notification()
        else:
            print("Failed to retrieve Chrome version. Please install google chrome on your operating system")
    return okay_to_run

#vars
chrome_webdriver_path = find_chrome_webdriver()
chrome_version = get_chrome_version()

