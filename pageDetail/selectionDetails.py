from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class selections:
    
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
        # Wait for form to generate
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='search-container']"))
        )

    def setEquipmentSelection(self):

        # Equipment Selection:
        self.driver.find_element_by_css_selector("#mat-select-1").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-option[@id='mat-option-7']")))
        self.driver.find_element_by_xpath("//mat-option[@id='mat-option-7']").click()


    def setPartySize(self, size):
        # Party Size:
        party = self.driver.find_element_by_id('mat-input-3')
        party.clear()
        party.send_keys(size)


    def setServiceType(self, serviceType):
        # Expand Filter field:
        self.driver.find_element_by_css_selector("button[id='filterButton'] span").click()
        self.driver.find_element_by_css_selector("button[id='consentButton'] span[class='mat-button-wrapper']").click()

        '''
        element = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#mat-select-5"))
        )
        '''
        # Service type:
        # service = driver.find_element_by_css_selector("mat-select[id='mat-select-5'] div[class='mat-select-value']")
        # service.click()
        # driver.find_element_by_xpath("//mat-option[@id='mat-option-116']").click()
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
            dates = self.driver.find_elements_by_css_selector("[class*='mat-calendar-body-cell mat-focus-indicator ng-star-inserted'] div")
            for date in dates:
                if arrivalDay == date.text:
                    date.click()
                    break
            
            pass 
        else:
            # Select Date
            dates = self.driver.find_elements_by_css_selector("[class*='mat-calendar-body-cell mat-focus-indicator ng-star-inserted'] div")
            for date in dates:
                if arrivalDay == date.text:
                    date.click()
                    break
        # Set length of staying
        nightsInput = self.driver.find_element_by_id('mat-input-2')
        nightsInput.clear()
        nightsInput.send_keys(nights)




    def setLocation(self, location):
        self.driver.find_element_by_css_selector("mat-select[id='mat-select-0'] div[class='mat-select-value']").click()
        self.driver.find_element_by_xpath("//span[@class='mat-option-text'][normalize-space()='Algonquin - Lake Of Two Rivers Campground']").click()
        self.driver.find_element_by_css_selector("div[class='mat-checkbox-inner-container']").click()
        self.driver.find_element_by_css_selector('#actionSearch').click()



