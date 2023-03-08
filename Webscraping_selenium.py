from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 

path = r'C:\Users\JUAN ACOSTA\OneDrive - Vicman Services S.A.S\Scripts Python\chromedriver.exe'

options = Options()
options.set_capability('acceptIncecureCerts', True)

driver = webdriver.Chrome(path, chrome_options=options)
driver.get('https://192.168.30.5/stats/index.php')

Quitar_Connfi = driver.find_element(By.XPATH,'//*[@id="details-button"]')
Quitar_Connfi.click()

Quitar_Connfi2 = driver.find_element(By.XPATH,'//*[@id="proceed-link"]')
Quitar_Connfi2.click()



user = 'analista'
contraseña = 'analista1'

Lugar_usuario = driver.find_element(By.XPATH,'//*[@id="user"]')
Lugar_contraseña = driver.find_element(By.XPATH,'//*[@id="password"]')

Lugar_usuario.send_keys(user)
Lugar_contraseña.send_keys(contraseña)

Aceptar_Ingreso = driver.find_element(By.XPATH,'//*[@id="submit"]')
Aceptar_Ingreso.click()
