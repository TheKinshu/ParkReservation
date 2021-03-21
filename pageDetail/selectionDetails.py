from os import truncate
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class selections:
    
    toggle = True

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
        # Wait for form to generate
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='search-container']"))
        )

    def login(self, email, password):
        self.driver.find_element_by_css_selector('#login').click()
        self.driver.find_element_by_xpath("//button[@id='consentButton']//span[@class='mat-button-wrapper'][normalize-space()='I Consent']").click()
        self.driver.find_element_by_css_selector('#email').send_keys(email)
        self.driver.find_element_by_css_selector('#password').send_keys(password)
        self.driver.find_element_by_css_selector("button[type='submit']").click()    

    def setEquipmentSelection(self, equipment):

        # Equipment Selection:
        self.driver.find_element_by_css_selector("#mat-select-1").click()

        equipments = self.driver.find_elements_by_css_selector('mat-option')

        for equipe in equipments:
            if equipment == equipe.text:
                equipe.click()
                break

    def setPartySize(self, size):
        # Party Size:
        party_size = self.driver.find_element_by_css_selector('#mat-input-5')
        party_size.clear()
        party_size.send_keys(size)


    def setServiceType(self, serviceType):
        # Expand Filter field:
        self.driver.find_element_by_css_selector("button[id='filterButton'] span").click()

        service = self.driver.find_element_by_css_selector("mat-select[id='mat-select-7'] div[class='mat-select-value']")
        service.click()
        services = self.driver.find_elements_by_css_selector('div mat-option span')

        for serv in services:
            if serv.text == serviceType:
                serv.click()
                break

    def setDates(self, arrivalMonth, arrivalDay, nights):
        # Date Arrival:
        self.driver.find_element_by_css_selector("mat-form-field[aria-label='Arrival date'] div[class='mat-form-field-infix']").click()
        date = self.driver.find_element_by_css_selector("button[id='monthDropdownPicker'] span[class='mat-button-wrapper']").text

        if not arrivalMonth in date:
            # Select Different Month
            self.driver.find_element_by_css_selector("button[id='monthDropdownPicker'] ").click()
            months = self.driver.find_elements_by_class_name('mat-calendar-body-cell-content')
            for month in months:
                arrivalMonth = arrivalMonth.upper()
                # Cycling through each row to find the desired month
                if arrivalMonth == month.text:
                    month.click()
                    break
                
            # Select Date
            self.driver.find_element_by_xpath("//div[normalize-space()='" + arrivalDay + "']").click()
            
        else:
            # Select Date
            dates = self.driver.find_elements_by_css_selector("[class*='mat-calendar-body-cell mat-focus-indicator ng-star-inserted'] div")
            for date in dates:
                if arrivalDay == date.text:
                    date.click()
                    break
            # Set length of staying
        nightsInput = self.driver.find_element_by_id('mat-input-4')
        nightsInput.clear()
        nightsInput.send_keys(nights)


    def consentClick(self):
        self.driver.find_element_by_css_selector("div[class='mat-checkbox-inner-container']").click()


    def setLocation(self, location):
        self.driver.find_element_by_css_selector('#mat-select-0').click()
        
        maps = self.driver.find_elements_by_css_selector('mat-option')

        for map in maps:
            if location == map.text:
                map.click()
                break
    def submiteInfo(self):
        self.driver.find_element_by_css_selector('#actionSearch').click()