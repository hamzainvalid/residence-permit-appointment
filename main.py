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
from version_checker import webdriver_checker
import sys

#first step: check for the existence of the webdriver and chrome version to make sure that the program runs wihtout any problems
check_for_webdriver = webdriver_checker()
if check_for_webdriver == False:
    sys.exit()

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
driver_path = input('Cogratulations your version check has pass!\n''Please copy and paste the path of your webdriver here to initiate the program! Please do not add any speech marks or anything just paste the path as it is: ')
country = input('Please enter your nationality! First letter must be capital and the rest should be small!: ')

number_of_people = int(input('Please enter the number of people applying! 1,2,3....: '))
people_in_german = ['eine Person','zwei Personen', 'drei Personen', 'vier Personen', 'fünf Personen', 'sechs Personen', 'sieben Personen', 'acht Personen']
number_of_people_in_german = people_in_german[number_of_people-1]

family_members = input('Do you live with any family members? Please type y/n! No input or inappropriate input will be considered as No!: ')
if family_members == 'y' or 'Y' or 'Yes' or 'yes':
    family_members_in_german = 'ja'
else:
    family_members_in_german = 'nein'


#chrome driver
chrome_driver_path = driver_path

#disable the chrome detection
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

#start the selenium service
service = Service(chrome_driver_path)
service.start()

#appointment booking website
driver = webdriver.Chrome(service=service, options=options)
website_url = "https://otv.verwalt-berlin.de/ams/TerminBuchen"
driver.get(website_url)


#automation
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
family_member_options.select_by_visible_text(family_members_in_german)
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
time.sleep(8)

while driver.find_element(By.ID, 'messagesBox'):
    final_button()
    time.sleep(8)

user_notification()





# Don't forget to stop the service and close the browser when you're done
# driver.quit()
# service.stop()