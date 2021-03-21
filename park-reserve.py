from pageDetail.siteSelection import siteSelection
from pageDetail.loginInfo import loginInfo
from selenium import webdriver
from pageDetail.selectionDetails import selections
import time



userInfo = {}

with open('camp.txt') as f:
    for line in f:
        (key, val) = line.split(':')
        userInfo[key] = val


chrome_options = webdriver.ChromeOptions()
headlessMode = str(userInfo['HeadlessChrome']).strip()
if ('yes' or 'true') in headlessMode.lower():
    # Start chrome in headless mode
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
else:
    # Visible Chrome
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://reservations.ontarioparks.com/')
driver.maximize_window()

driver.implicitly_wait(10)


email = str(userInfo['Username']).strip()
password = str(userInfo['Password']).strip()

partySize = int(userInfo['partySize'])
serviceType = str(userInfo['serviceType']).strip()

equipment =  str(userInfo['Equipment']).strip()
arrivalMonth = str(userInfo['MonthOfArrival']).strip()
arrivalDay = str(userInfo['DateOfArrival']).strip()
nights = int(userInfo['NightStayed'])
campsite = str(userInfo['Campsite']).strip()

try:
    # Login
    login = loginInfo(driver)
    login.login(email, password)

    # Create Reservation
    driver.find_element_by_css_selector('#newReservation').click()

    time.sleep(4)

    # Initializing selection page
    selection = selections(driver)

    # Select Location
    selection.setLocation(campsite)

    # Click consent
    selection.consentClick()
    
    selection.setEquipmentSelection(equipment)

    selection.setPartySize(partySize)

    # Date Arrival:
    selection.setDates(arrivalMonth, arrivalDay, nights)
    
    selection.setServiceType(serviceType)

    selection.submiteInfo()

    driver.find_element_by_css_selector("button[aria-label='Expand park alerts']").click()

    # Initializing site selection page
    siteSelect = siteSelection(driver)
    # Find available campground
    siteSelect.findCampground()
    # Find available site
    siteSelect.findSite()
    
finally:
    pass