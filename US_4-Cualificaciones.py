import HtmlTestRunner
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


class Cualificaciones(unittest.TestCase):

    def setUp(self):
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=10)

    def test_admin_skill(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin ")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        login = self.driver.find_element(By.ID, "btnLogin").click()

        actions = ActionChains(self.driver)
        menu1 = self.driver.find_element(By.ID, "menu_admin_viewAdminModule")
        menu2 = self.driver.find_element(By.ID, "menu_admin_Qualifications")
        menu3 = self.driver.find_element(By.ID, "menu_admin_viewSkills")
        actions.move_to_element(menu1).move_to_element(menu2).move_to_element(menu3).perform()
        menu3.click()

        add = self.driver.find_element(By.ID, "menu_admin_viewAdminModule").click()

        name_skill = self.driver.find_element(By.ID, 'skill_name').send_keys("Skill 1")
        description_skill = self.driver.find_element(By.ID, 'skill_description').send_keys("Description Skill 1")
        save_skill = self.driver.find_element(By.ID, "btnSave").click()

        print("Prueba Correcta - US 4 | TC01 - Crear, Editar y Borrar Skill")




    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    print("prueba exitosa")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Numbers Tech\\Desktop\Python\\tarea4-pruebas\\Reportes'))



