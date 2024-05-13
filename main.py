from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

# c = webdriver.ChromeOptions()
# c.add_argument("--incognito")
# run = webdriver.Chrome(executable_path="D:\\Github Repositories\\residence-permit-appointment\\chrome driver\\chromedriver-win64\\chromedriver.exe", options=c)
# run.get('https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en&termin=1&dienstleister=327437&anliegen[]=324661&herkunft=1')

# Specify the path to the ChromeDriver executable
chrome_driver_path = "D:\\Github Repositories\\residence-permit-appointment\\chrome driver\\chromedriver-win64\\chromedriver.exe"

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

# Create a Service object
service = Service(chrome_driver_path)

# Start the WebDriver service
service.start()

# Create a WebDriver instance with the service
driver = webdriver.Chrome(service=service, options=options)

# URL of the website you want to visit
website_url = "https://otv.verwalt-berlin.de/ams/TerminBuchen"

# Open the website
driver.get(website_url)

# Find all elements with class name 'button'
buttons = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "button"))
)

# Iterate over the buttons
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

# Now you can interact with the website
# l = driver.find_elements(By.CLASS_NAME, 'button')
# #time.sleep(5)
# for i in l:
#     if i.text == 'Termin buchen':
#         i.click()

# Locate the checkbox element by its ID (replace 'checkbox_id' with the actual ID of the checkbox)
checkbox = driver.find_element(By.CLASS_NAME, "XCheckbox")
# Check the checkbox if it's not already checked
if not checkbox.is_selected():
    checkbox.click()
time.sleep(3)

further_button = driver.find_element(By.NAME, "applicationForm:managedForm:proceed").click()
time.sleep(12)

country_select = driver.find_element(By.NAME, 'sel_staat')
country_options = Select(country_select)
country_options.select_by_visible_text("Pakistan")
time.sleep(2)

number_of_people_select = driver.find_element(By.NAME, 'personenAnzahl_normal')
number_of_people_options = Select(number_of_people_select)
number_of_people_options.select_by_visible_text('eine Person')
time.sleep(2)

family_member_select = driver.find_element(By.NAME, 'lebnBrMitFmly')
family_member_options = Select(family_member_select)
family_member_options.select_by_visible_text('nein')
time.sleep(2)

service_option = driver.find_element(By.CLASS_NAME, 'kachel-461-0-1').click()
time.sleep(4)

type1_option = driver.find_element(By.CLASS_NAME, 'accordion-461-0-1-1').click()
time.sleep(4)
type2_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "SERVICEWAHL_DE461-0-1-1-324661"))
)
time.sleep(5)

final_button = driver.find_element(By.ID, 'applicationForm:managedForm:proceed').click()








# Don't forget to stop the service and close the browser when you're done
# driver.quit()
# service.stop()

# l = run.find_elements(By.CLASS_NAME, 'button')
# #time.sleep(5)
# for i in l:
#     if i.text == 'Book Appointment':
#         i.click()
#
# if len(run.find_elements(By.NAME, 'gelesen')) < 2:
#     run.find_element(By.NAME, 'gelesen').click()
#     if len(run.find_elements(By.NAME, 'applicationForm:managedForm:proceed')) < 2:
#         run.find_element(By.NAME, 'applicationForm:managedForm:proceed').click()
#         print('clicked2')
#     print('clicked')
# else:
#     print('more than one')