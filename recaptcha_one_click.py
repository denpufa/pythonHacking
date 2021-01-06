from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/Murilo Henrique/Desktop/chromedriver.exe" 
driver = webdriver.Chrome(path)
driver.get('https://rodolfodantas.com.br/contato')
tela = driver.current_window_handle  


def enviarEmail() :  
    texto = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".text-area")))
    texto.send_keys("vc foi ludibriado :)")
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    capCheck = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
        )
    time.sleep(1)
    capCheck.click()
    time.sleep(4)
    driver.switch_to_window(tela)
    botao = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id1609050065228 .rich-text-element-content")))
    botao.click()

for x in range(1):
    enviarEmail()
    


 



