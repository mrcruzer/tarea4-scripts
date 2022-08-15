import HtmlTestRunner
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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

        empleado_name = self.driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("Alice Duval")

        username = self.driver.find_element(By.ID,"systemUser_userName").send_keys("usuario1")

        status = self.driver.find_element(By.ID,"systemUser_status")
        status.is_selected()

        password = self.driver.find_element(By.ID,"systemUser_password").send_keys("CERtificado14")
        confirm_password = self.driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("CERtificado14")

        guardar = self.driver.find_element(By.ID,"btnSave").click()



   '''def test_buscar_usuario(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin12345")
        login = self.driver.find_element(By.ID, "btnLogin").click()
        admin = self.driver.find_element(By.ID, "menu_admin_viewAdminModule").click()



   def tearDown(self):
        self.driver.quit()'''




if __name__ == '__main__':
    print("prueba exitosa")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Numbers Tech\\Desktop\Python\\tarea4-pruebas\\Reportes'))



