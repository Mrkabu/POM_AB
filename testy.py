
#  from Login import LoginPage
from definicje import Start
import unittest
from selenium import webdriver
#from slownik import kliknij

class Test(unittest.TestCase):

    def test_valid_login(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\Python\Drivery\chromedriver.exe")
        self.driver.get('https://ncplusgo.pl')
        self.driver.maximize_window()

        #kliknij(self.driver, 'zaloguj')
        #return
        log_in = Start(self.driver)
        log_in.zalogujClick()
        #log_in_2 = Start(self.driver)
        log_in.terazwtvClick()


#  W celu zamkniecia przegladarki mozna dodac:

    #  def tearDown(self):
        #  self.driver.quit()

if __name__ == '__main__':
    unittest.main()