from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from notification_sound import user_notification
import sys

#readme

print('Please read the read me file before using the app it is highly recommended.\n Click this link to readme file for instructions: https://github.com/hamzainvalid/residence-permit-appointment/blob/main/README.md \n Please read the usage if you encounter any error or find any kind of problem with running the program')
input('Press enter to begin')

print('Please do not type anything or close the window until required by the program to avoid interruptions!')
time.sleep(3)

def retry_action(action, max_retries=3):
    retry_count = 0
    while True:
        try:
            action()
            break
        except StaleElementReferenceException as e:
            if retry_count < max_retries:
                print(f"Retry {retry_count + 1}: {e}")
                retry_count += 1
            else:
                raise e

def final_button():
    driver.find_element(By.ID, 'applicationForm:managedForm:proceed').click()

#vars
driver_path = input('Please input the webdriver path here')
counter = 0
appointment_found = False

print('Please input the correct information for the following questions with correct format to avoid any interruption in program running. Refer to readme instructions')
time.sleep(3)

country = input('Please enter your country name in German wihtout any suffixes or prefixes! First letter must be capital and the rest should be small! ex: Pakistan: ')

number_of_people = int(input('Please enter the number of people applying! Numbers only ex: 1,2,3....: Max 8, Min 1'))
people_in_german = ['eine Person','zwei Personen', 'drei Personen', 'vier Personen', 'fünf Personen', 'sechs Personen', 'sieben Personen', 'acht Personen']
number_of_people_in_german = people_in_german[number_of_people-1]

print('Living with family member is by default "No" at the moment, it will soon be available.')

print('Your data has been noted. The program will now check the compatibility of the webdriver and then the Chrome window will now open, please do not type or click anything on the window or the terminal and have pateince, you are not required to do anything now, it will take some time to process. Once the program finishes running or encounters an error the chrome window will automatically close. Please refer to the readme.')
time.sleep(5)
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


def run_program():
    # Path to the ChromeDriver
    chrome_driver_path = driver_path

    # Check if the ChromeDriver path is correct
    import os
    if not os.path.exists(chrome_driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}. Please check the path and try again.")

    # Set up the WebDriver
    driver = setup_driver(chrome_driver_path)

    # reset the counter
    counter = 0
    # webdriver path
    chrome_driver_path = driver_path

    # disable the chrome detection
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")

    # start the selenium service
    service = Service(chrome_driver_path)
    service.start()

    # appointment booking website
    driver = webdriver.Chrome(service=service, options=options)
    website_url = "https://otv.verwalt-berlin.de/ams/TerminBuchen"
    driver.get(website_url)

    # automation
    buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "button"))
    )

    for button in buttons:
        try:
            # Check if the button's text is 'Termin buchen'
            if button.text == 'Termin buchen':
                # Click the button
                button.click()
        except StaleElementReferenceException:
            # If element becomes stale, re-locate it
            buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "button"))
            )
            continue
    time.sleep(3)

    checkbox = driver.find_element(By.CLASS_NAME, "XCheckbox")
    # Check the checkbox if it's not already checked
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(3)

    further_button = driver.find_element(By.NAME, "applicationForm:managedForm:proceed").click()
    time.sleep(12)

    country_select = driver.find_element(By.NAME, 'sel_staat')
    country_options = Select(country_select)
    country_options.select_by_visible_text(country)
    time.sleep(2)

    number_of_people_select = driver.find_element(By.NAME, 'personenAnzahl_normal')
    number_of_people_options = Select(number_of_people_select)
    number_of_people_options.select_by_visible_text(number_of_people_in_german)
    time.sleep(2)

    family_member_select = driver.find_element(By.NAME, 'lebnBrMitFmly')
    family_member_options = Select(family_member_select)
    family_member_options.select_by_visible_text('nein')
    time.sleep(2)

    service_option = driver.find_element(By.CLASS_NAME, 'kachel-461-0-1').click()
    time.sleep(4)

    type1_option = driver.find_element(By.CLASS_NAME, 'accordion-461-0-1-1').click()
    time.sleep(4)

    for i in driver.find_elements(By.CLASS_NAME, 'level3'):
        time.sleep(2)
        element = i.find_element(By.XPATH, './/label')
        if element.text == 'Aufenthaltserlaubnis für Fachkräfte zur Arbeitsplatzsuche - Erteilung (§ 20)':
            element.click()
            break
    time.sleep(5)

    final_button()
    time.sleep(10)

    while driver.find_element(By.ID, 'messagesBox'):
        if counter == 20:
            run_program()
        counter += 1
        final_button()
        time.sleep(10)
    appointment_found = True


if appointment_found == False:
    run_program()


print('Congratulations, the appointment is found. Please fill in your information and book the appointment the notification sound will go off automatically, do not close chrome or the program window(Terminal)')
user_notification()
input("Press Enter to exit...")
