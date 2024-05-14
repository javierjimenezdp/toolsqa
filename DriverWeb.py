## Test unitarios
import unittest
## Selenium
from selenium import webdriver

## Clase para configurar el webdriver
class webdriverSetup(unittest.TestCase):
    ## Método que se ejecuta antes de cada prueba
    def setUp(self):
        ## Inicializa el webdriver de Selenium (en este caso, Chrome)
        self.driver = webdriver.Chrome()
    ## Método que se ejecuta después de cada prueba
    def tearDown(self):
        ## Cierra el navegador después de cada prueba
        self.driver.quit()
