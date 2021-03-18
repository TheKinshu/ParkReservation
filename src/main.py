from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import selenium


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://reservations.ontarioparks.com/')
driver.maximize_window()

driver.implicitly_wait(6)
equipError = False
wait = WebDriverWait(driver, 4)

try:
    # Wait for form to generate
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='search-container']"))
    )
    
    # Equipment Selection:
    driver.find_element_by_css_selector("#mat-select-1").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option[@id='mat-option-7']")))
    equipment = driver.find_element_by_xpath("//mat-option[@id='mat-option-7']").click()
    
finally:

    # Party Size:
    partySize = 3
    party = driver.find_element_by_id('mat-input-3')
    party.clear()
    party.send_keys(partySize)

    # Expand Filter field:
    driver.find_element_by_css_selector("button[id='filterButton'] span").click()
    driver.find_element_by_css_selector("button[id='consentButton'] span[class='mat-button-wrapper']").click()

    element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#mat-select-7"))
    )

    # Service type:
    service = driver.find_element_by_css_selector("mat-select[id='mat-select-7'] div[class='mat-select-value']")
    service.click()
    driver.find_element_by_xpath("//mat-option[@id='mat-option-126']").click()

    # Date Arrival:
    driver.find_element_by_css_selector("mat-form-field[aria-label='Arrival date'] div[class='mat-form-field-infix']").click()
    date = driver.find_element_by_css_selector("button[id='monthDropdownPicker'] span[class='mat-button-wrapper']").text

    arrivalMonth = 'Aug'
    arrivalDay = '30'
    nights = 7

    if not arrivalMonth in date:
        # Select Different Month
        driver.find_element_by_css_selector("button[id='monthDropdownPicker'] ").click()
        months = driver.find_elements_by_class_name('mat-calendar-body-cell-content')
        for month in months:
            arrivalMonth = arrivalMonth.upper()
            # Cycling through each row to find the desired month
            if arrivalMonth == month.text:
                month.click()
                break
        
        # Select Date
        dates = driver.find_elements_by_css_selector("[class*='mat-calendar-body-cell mat-focus-indicator ng-star-inserted'] div")
        for date in dates:
            if arrivalDay == date.text:
                date.click()
        
        pass 
    else:
        # Select Date
        dates = driver.find_elements_by_css_selector("[class*='mat-calendar-body-cell mat-focus-indicator ng-star-inserted'] div")
        for date in dates:
            if arrivalDay == date.text:
                date.click()


    nightsInput = driver.find_element_by_id('mat-input-2')
    nightsInput.clear()
    nightsInput.send_keys(nights)

    # Location:
    
    driver.find_element_by_css_selector("mat-select[id='mat-select-0'] div[class='mat-select-value']").click()
    driver.find_element_by_xpath("//span[@class='mat-option-text'][normalize-space()='Algonquin - Lake Of Two Rivers Campground']").click()

    driver.find_element_by_css_selector("div[class='mat-checkbox-inner-container']").click()


    # Equipment Selection:
    driver.find_element_by_css_selector("#mat-select-1").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option[@id='mat-option-7']")))
    equipment = driver.find_element_by_xpath("//mat-option[@id='mat-option-7']").click()

    party = driver.find_element_by_id('mat-input-3')
    party.clear()
    party.send_keys(partySize)

    driver.find_element_by_css_selector('#actionSearch').click()

    driver.find_element_by_id('list-view-button').click()
    avali = driver.find_elements_by_css_selector('span mat-panel-description div')
    for ava in avali:
        if ava.text == 'Available':
            ava.click()
    pass

