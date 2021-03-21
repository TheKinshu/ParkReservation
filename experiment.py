from selenium import webdriver
from pageDetail.selectionDetails import selections
from pageDetail.siteSelection import siteSelection

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://reservations.ontarioparks.com/')
driver.maximize_window()

driver.implicitly_wait(6)

partySize = 3
serviceType = 'Electric'

arrivalMonth = 'Aug'
arrivalDay = '30'
nights = 7

try:
    # Initializing selection page
    selection = selections(driver)
    
    # Select equipment type 
    selection.setEquipmentSelection()
    
    # Set party size
    selection.setPartySize(partySize)
    
    # Set service type
    selection.setServiceType(serviceType)

    # Re-select/enter equipment and party size for page timeout
    selection.setEquipmentSelection()
    selection.setPartySize(partySize)

    selection.setDates(arrivalMonth, arrivalDay, nights)

    # Location:
    selection.setLocation(None)
    # Initializing site selection page
    siteSelect = siteSelection(driver)
    # Find available campground
    siteSelect.findCampground()
    # Find available site
    siteSelect.findSite()


finally:
    # Close driver 
    driver.close()
    pass