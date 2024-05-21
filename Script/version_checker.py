import subprocess
import re

def get_chrome_version():
    try:
        # Run the command to get the Chrome version
        result = subprocess.run(
            ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        # Check if the command was executed successfully
        if result.returncode == 0:
            # Extract and return the version from the output
            version = result.stdout.strip()
            version_number = re.search(r'(\d+\.\d+\.\d+\.\d+)', version).group(1)
            return version_number
        else:
            print("Error getting Chrome version:", result.stderr)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_webdriver_version():
    try:
        # Run the command to get the Chrome WebDriver version
        result = subprocess.run(
            ["chromedriver", "--version"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        # Check if the command was executed successfully
        if result.returncode == 0:
            # Extract and return the version from the output
            version = result.stdout.strip()
            version_number = re.search(r'(\d+\.\d+\.\d+\.\d+)', version).group(1)
            return version_number
        else:
            print("Error getting WebDriver version:", result.stderr)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_webdriver_path():
    try:
        # Run the 'which' command to find the path of chromedriver
        result = subprocess.run(
            ["which", "chromedriver"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        # Check if the command was executed successfully
        if result.returncode == 0:
            # Extract and return the path from the output
            webdriver_path = result.stdout.strip()
            return webdriver_path
        else:
            print("Error finding WebDriver path:", result.stderr)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def download_webdriver_notification():
    str(chrome_version)
    chrome_version_initaials = int(chrome_version[:3])
    if chrome_version_initaials == 115 or chrome_version_initaials > 115:
        print(f'The program could not find the correct webdriver in the provided locations. Please download the webdriver version: {chrome_version_initaials} using this link:'+'https://googlechromelabs.github.io/chrome-for-testing/')
    else:
        print(f'The program could not find the correct webdriver in the provided locations. Please download the webdriver version:{chrome_version_initaials} using this link:'+'https://chromedriver.chromium.org/downloads')





def webdriver_checker():
    okay_to_run = False
    if webdriver_version:
        print("Chrome WebDriver found at:", webdriver_version)
        str(chrome_version)
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
chrome_version = get_chrome_version()
webdriver_version = get_webdriver_version()
chrome_webdriver_path = get_webdriver_path()

