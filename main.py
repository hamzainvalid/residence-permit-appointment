from selenium import webdriver
from selenium.webdriver.common.by import By
import time


c = webdriver.ChromeOptions()
c.add_argument("--incognito")
run = webdriver.Chrome(executable_path="D:\\Github Repositories\\residence-permit-appointment\\chrome driver\\chromedriver-win64\\chromedriver.exe", options=c)
run.get('https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en&termin=1&dienstleister=327437&anliegen[]=324661&herkunft=1')



l = run.find_elements(By.CLASS_NAME, 'button')
#time.sleep(5)
for i in l:
    if i.text == 'Book Appointment':
        i.click()

if len(run.find_elements(By.NAME, 'gelesen')) < 2:
    run.find_element(By.NAME, 'gelesen').click()
    if len(run.find_elements(By.NAME, 'applicationForm:managedForm:proceed')) < 2:
        run.find_element(By.NAME, 'applicationForm:managedForm:proceed').click()
        print('clicked2')
    print('clicked')
else:
    print('more than one')