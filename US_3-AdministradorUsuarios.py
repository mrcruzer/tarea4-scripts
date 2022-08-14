import HtmlTestRunner
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AdministradorUsuarios(unittest.TestCase):

    def setUp(self):
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=10)

    def test_creacion_usuario(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin ")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        login = self.driver.find_element(By.ID, "btnLogin").click()
        admin = self.driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        agregar = self.driver.find_element(By.XPATH, "//input[@id='btnAdd']").click()

        rol = self.driver.find_element(By.ID, "systemUser_userType")
        rol.is_selected()

        print("Prueba Correcta - US 3 |  TC01 | Validar Login Usuario Correcto")



    '''def test_login_page_incorrect(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin12345")
        login = self.driver.find_element(By.ID, "btnLogin").click()
        #welcome = self.driver.find_element(By.ID, 'welcome').click()
        msj = self.driver.find_element(By.XPATH, "//span[@id='spanMessage']")
        self.assertTrue(msj)
        print("Prueba Correcta - US 1 | TC02 | Validar Login Usuario Incorrecto")'''



    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    print("prueba exitosa")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Numbers Tech\\Desktop\Python\\tarea4-pruebas\\Reportes'))



