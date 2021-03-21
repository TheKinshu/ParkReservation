class loginInfo:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element_by_css_selector('#login').click()
        self.driver.find_element_by_xpath("//button[@id='consentButton']//span[@class='mat-button-wrapper'][normalize-space()='I Consent']").click()
        self.driver.find_element_by_css_selector('#email').send_keys(email)
        self.driver.find_element_by_css_selector('#password').send_keys(password)
        self.driver.find_element_by_css_selector("button[type='submit']").click()