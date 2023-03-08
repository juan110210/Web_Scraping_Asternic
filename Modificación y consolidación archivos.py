from selenium import webdriver
import time

edge_options = webdriver.EdgeOptions()
edge_options.set_capability('acceptInsecureCerts', True)

url = 'https://www.udemy.com/'
path = r'C:\Users\JUAN ACOSTA\OneDrive - Vicman Services S.A.S\Scripts Python\msedgedriver'

driver = webdriver.Edge(executable_path=path, options=edge_options)
driver.get(url)

time.sleep(15)
