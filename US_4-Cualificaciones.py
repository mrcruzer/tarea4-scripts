import HtmlTestRunner
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


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

        add = self.driver.find_element(By.ID, "btnAdd").click()

        name_skill = self.driver.find_element(By.ID, 'skill_name').send_keys("Skill 1")
        description_skill = self.driver.find_element(By.ID, 'skill_description').send_keys("Description Skill 1")
        save_skill = self.driver.find_element(By.ID, "btnSave").click()

        filas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//thead//tr"))
        columnas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//tbody//tr[1]/td"))

        #print(filas)
        #print(columnas)

        for f in range(2, filas+1):
            print(f)

        for f in range(2, filas + 1):
            for c in range(1, columnas + 1):
                valores = self.driver.find_element(By.XPATH,"//table[id='recordsListTable']//tbody//tr[" + str(f) + "]/td[" + str(c) + "]").text.__contains__("Skill 1")
                valores.click()

        name_skill = self.driver.find_element(By.ID, 'skill_name').send_keys("Skill 2")
        description_skill = self.driver.find_element(By.ID, 'skill_description').send_keys("Description Skill 2")
        save_skill = self.driver.find_element(By.ID, "btnSave").click()

        print("Prueba Correcta - US 4 | TC01 - Crear, Editar y Borrar Skill")

    def test_admin_education(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin ")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        login = self.driver.find_element(By.ID, "btnLogin").click()

        actions = ActionChains(self.driver)
        menu1 = self.driver.find_element(By.ID, "menu_admin_viewAdminModule")
        menu2 = self.driver.find_element(By.ID, "menu_admin_Qualifications")
        menu3 = self.driver.find_element(By.ID, "menu_admin_viewEducation")
        actions.move_to_element(menu1).move_to_element(menu2).move_to_element(menu3).perform()
        menu3.click()

        add = self.driver.find_element(By.ID, "btnAdd").click()

        level = self.driver.find_element(By.ID, 'education_name').send_keys("Education 1")
        save_level = self.driver.find_element(By.ID, "btnSave").click()

        filas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//thead//tr"))
        columnas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//tbody//tr[1]/td"))

            # print(filas)
            # print(columnas)

        for f in range(2, filas + 1):
            print(f)

        for f in range(2, filas + 1):
            for c in range(1, columnas + 1):
                valores_education = self.driver.find_element(By.XPATH, "//table[id='recordsListTable']//tbody//tr[" + str(f) + "]/td[" + str(c) + "]").text.__contains__("Education 1")
                valores_education.click()

        level = self.driver.find_element(By.ID, 'education_name').send_keys("Education 2")
        save_level = self.driver.find_element(By.ID, "btnSave").click()

        print("Prueba Correcta - US 4 | TC02 - Crear, Editar y Borrar Education")

    def test_admin_licenses(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin ")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        login = self.driver.find_element(By.ID, "btnLogin").click()

        actions = ActionChains(self.driver)
        menu1 = self.driver.find_element(By.ID, "menu_admin_viewAdminModule")
        menu2 = self.driver.find_element(By.ID, "menu_admin_Qualifications")
        menu3 = self.driver.find_element(By.ID, "menu_admin_viewLicenses")
        actions.move_to_element(menu1).move_to_element(menu2).move_to_element(menu3).perform()
        menu3.click()

        add = self.driver.find_element(By.ID, "btnAdd").click()

        license_name = self.driver.find_element(By.ID, 'license_name').send_keys("License 1")
        save_license = self.driver.find_element(By.ID, "btnSave").click()

        filas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//thead//tr"))
        columnas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//tbody//tr[1]/td"))

            # print(filas)
            # print(columnas)

        for f in range(2, filas + 1):
            print(f)

        for f in range(2, filas + 1):
            for c in range(1, columnas + 1):
                valores_licenses = self.driver.find_element(By.XPATH, "//table[id='recordsListTable']//tbody//tr[" + str(f) + "]/td[" + str(c) + "]").text.__contains__("License 1")
                valores_licenses.click()

        license_name = self.driver.find_element(By.ID, 'license_name').send_keys("License 2")
        save_license = self.driver.find_element(By.ID, "btnSave").click()

        print("Prueba Correcta - US 4 | TC03 - Crear, Editar y Borrar License")


    def test_admin_languages(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin ")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        login = self.driver.find_element(By.ID, "btnLogin").click()

        actions = ActionChains(self.driver)
        menu1 = self.driver.find_element(By.ID, "menu_admin_viewAdminModule")
        menu2 = self.driver.find_element(By.ID, "menu_admin_Qualifications")
        menu3 = self.driver.find_element(By.ID, "menu_admin_viewLanguages")
        actions.move_to_element(menu1).move_to_element(menu2).move_to_element(menu3).perform()
        menu3.click()

        add = self.driver.find_element(By.ID, "btnAdd").click()

        language_name = self.driver.find_element(By.ID, 'language_name').send_keys("Languages 1")
        save_lenguage = self.driver.find_element(By.ID, "btnSave").click()

        filas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//thead//tr"))
        columnas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//tbody//tr[1]/td"))

            # print(filas)
            # print(columnas)

        for f in range(2, filas + 1):
            print(f)

        for f in range(2, filas + 1):
            for c in range(1, columnas + 1):
                valores_lenguage = self.driver.find_element(By.XPATH, "//table[id='recordsListTable']//tbody//tr[" + str(f) + "]/td[" + str(c) + "]").text.__contains__("Language 1")
                valores_lenguage.click()

        language_name = self.driver.find_element(By.ID, 'language_name').send_keys("Language 2")
        save_lenguage = self.driver.find_element(By.ID, "btnSave").click()


        print("Prueba Correcta - US 4 | TC04 - Crear, Editar y Borrar Language")


    def test_admin_membership(self):
        usuario = self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin ")
        password = self.driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        login = self.driver.find_element(By.ID, "btnLogin").click()

        actions = ActionChains(self.driver)
        menu1 = self.driver.find_element(By.ID, "menu_admin_viewAdminModule")
        menu2 = self.driver.find_element(By.ID, "menu_admin_Qualifications")
        menu3 = self.driver.find_element(By.ID, "menu_admin_membership")
        actions.move_to_element(menu1).move_to_element(menu2).move_to_element(menu3).perform()
        menu3.click()

        add = self.driver.find_element(By.ID, "btnAdd").click()

        membership_name = self.driver.find_element(By.ID, 'membership_name').send_keys("Membership 1")
        save_skill = self.driver.find_element(By.ID, "btnSave").click()

        filas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//thead//tr"))
        columnas = len(self.driver.find_elements(By.XPATH, "//table[@id='recordsListTable']//tbody//tr[1]/td"))

            # print(filas)
            # print(columnas)

        for f in range(2, filas + 1):
            print(f)

        for f in range(2, filas + 1):
            for c in range(1, columnas + 1):
                valores_membership = self.driver.find_element(By.XPATH, "//table[id='recordsListTable']//tbody//tr[" + str(f) + "]/td[" + str(c) + "]").text.__contains__("Membership 1")
                valores_membership.click()

        membership_name = self.driver.find_element(By.ID, 'membership_name').send_keys("Membership 2")
        save_membership = self.driver.find_element(By.ID, "btnSave").click()

        print("Prueba Correcta - US 4 | TC05 - Crear, Editar y Borrar Membership")




    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    print("prueba exitosa")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Numbers Tech\\Desktop\Python\\tarea4-pruebas\\Reportes'))



