## Importa la clase homePage del archivo homePage.py
from HomePage import homePage
## Importa la clase webdriverSetup del archivo driverWeb.py
from DriverWeb import webdriverSetup

## Clase de prueba que hereda de webdriverSetup
class test_katalon(webdriverSetup):
    ## Método para realizar una cita médica
    def make_appointment(self):
        ## Configura el entorno para la prueba
        self.setUp()
        ## Obtiene el driver del navegador
        driver = self.driver
        ## Abre la URL de la página principal en el navegador
        self.driver.get(homePage(driver).getUrlKatalon)
        ## Crea una instancia de la clase homePage
        pageHome = homePage(driver)

## Crea una instancia de la clase de prueba y ejecuta el método para realizar una cita médica
test = test_katalon()
test.make_appointment()
