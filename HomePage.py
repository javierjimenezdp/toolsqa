## Librerías Selenium
from selenium.webdriver.common.by import By
"""Esto importa la clase By de Selenium, que se utiliza para seleccionar 
    elementos en la página web por medio de diferentes criterios como ID, 
    nombre, clase, etc."""
    
from selenium.webdriver.support.ui import WebDriverWait
"""Esto importa la clase WebDriverWait de Selenium, que se utiliza para 
esperar a que ciertas condiciones se cumplan antes de continuar con el código."""

from selenium.webdriver.support import expected_conditions as EC
"""Esto importa la clase expected_conditions de Selenium, que se utiliza 
en combinación con WebDriverWait para especificar las condiciones 
que se deben cumplir antes de continuar con el código."""

## Clase que representa la página principal
class homePage:
    """Aquí se define una clase llamada homePage que representa 
    la página principal del sitio web."""
    
    ## URL de la página principal
    getUrlKatalon = "https://www.toolsqa.com/selenium-training/#enroll-form"
    """Aquí se define una clase llamada homePage que representa 
    la página principal del sitio web."""

    ## Método constructor que recibe el driver del navegador
    def __init__(self, driver):
        """Este es el método constructor de la clase homePage 
        que recibe el parámetro driver, que representa el navegador web."""
        
        ## Asigna el driver recibido como parámetro a un atributo de la clase
        self.driver = driver
        """Esta línea asigna el objeto driver recibido como parámetro 
        a un atributo de la clase llamado driver, para que pueda ser 
        utilizado en otros métodos de la clase."""

    ## Método para obtener la URL de la página principal
    def loginPage(self):
        """Este es un método de instancia de la clase homePage llamado 
        loginPage que no recibe ningún parámetro."""
        
        ## Retorna la URL de la página principal
        return self.getUrlKatalon
    """Este comando retorna la URL de la página principal almacenada 
    en la variable getUrlKatalon."""
