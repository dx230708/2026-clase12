from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators (Selectores)
        self.lbl_titulo = (By.CSS_SELECTOR, "div.header_secondary_container .title")
        self.items_productos = (By.CLASS_NAME, "inventory_item")
        self.btn_menu_hamburguesa = (By.ID, "react-burger-menu-btn")
        self.btn_filtros = (By.CLASS_NAME, "product_sort_container")
        self.btn_add_to_cart_primer_item = (By.CLASS_NAME, "btn_inventory")
        self.badge_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.icon_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.lbl_nombre_primer_producto = (By.CLASS_NAME, "inventory_item_name")

    def obtener_texto_titulo(self):
        elemento = self.wait.until(EC.visibility_of_element_located(self.lbl_titulo))
        return elemento.text

    def contar_productos_visibles(self):
        return len(self.driver.find_elements(*self.items_productos))

    def verificar_elementos_interfaz(self):
        menu = self.driver.find_element(*self.btn_menu_hamburguesa).is_displayed()
        filtros = self.driver.find_element(*self.btn_filtros).is_displayed()
        return menu and filtros

    def agregar_primer_producto_al_carrito(self):
        botones = self.wait.until(EC.presence_of_all_elements_located(self.btn_add_to_cart_primer_item))
        botones[0].click()

    def obtener_contador_carrito(self):
        # """Devuelve el texto del contador del carrito."""
        elemento = self.wait.until(EC.visibility_of_element_located(self.badge_carrito))
        return elemento.text

    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self.lbl_nombre_primer_producto)[0].text

    def ir_al_carrito(self):
		# """Hace clic en el ícono del carrito para navegar a la siguiente pantalla."""
         self.driver.find_element(*self.icon_carrito).click()

    def agregar_producto_por_xpath(self, xpath_producto):
        # """Busca y hace clic en el botón de agregar de un producto específico utilizando su ruta XPath dinámica provista por el archivo JSON."""
        elemento = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_producto)))
        elemento.click()