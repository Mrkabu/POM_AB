from locators import Locator


class Start(Locator):

    def __init__(self, driver):
        self.driver = driver
       # self.pobierz()

    #def pobierz(self):
        #self.zalogujElement = self.driver.find_element_by_xpath(self.zaloguj)
        #self.terazwtvElement = self.driver.find_element_by_xpath(self.terazwtv)


    def zalogujClick(self):
        self.zalogujElement = self.driver.find_element_by_xpath(self.zaloguj)
        self.zalogujElement.click()
       # self.pobierz()

    def terazwtvClick(self):

        self.terazwtvElement = self.driver.find_element_by_xpath(self.terazwtv)
        self.terazwtvElement.click()
      #  self.pobierz()