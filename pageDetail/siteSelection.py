class siteSelection:

    def __init__(self, driver) -> None:
        self.driver = driver

    def findCampground(self):
        self.driver.find_element_by_id('list-view-button').click()
        avali = self.driver.find_elements_by_css_selector('span mat-panel-description div')
        for ava in avali:
            if ava.text == 'Available':
                ava.click()
                break
        self.driver.find_element_by_css_selector("button[aria-label='Expand park alerts']").click()

    def findSite(self):
        siteFound = False
        siteNum = 0
        while siteFound == False:
            avali = self.driver.find_elements_by_css_selector('mat-accordion mat-expansion-panel')
            for ava in avali:
                siteNum = (ava.text).split()
                siteNum = int(siteNum[1])
                if 'Available' in ava.text and not('Partially' in ava.text):
                    ava.click()
                    siteFound = True
                    break
            if siteFound:
                break
            self.driver.find_element_by_id('loadMoreButton').click()
        
        reserveBtn = self.driver.find_element_by_id('reserveButton-' + str(siteNum-1))
        reserveBtn.click()