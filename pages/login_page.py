from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators (Selectores)
        self.txt_username = (By.ID, "user-name")
        self.txt_password = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")

    def navegar_a_login(self, url):
        self.driver.get(url)

    def login_exitoso(self, usuario, password):
        input_user = self.wait.until(EC.presence_of_element_located(self.txt_username))
        input_user.clear()
        input_user.send_keys(usuario)
        
        input_pass = self.driver.find_element(*self.txt_password)
        input_pass.clear()
        input_pass.send_keys(password)
        
        self.driver.find_element(*self.btn_login).click()