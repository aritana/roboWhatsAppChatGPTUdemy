from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os 


dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path +"profile/zap")
driver = webdriver.Chrome(chrome_options2)
#só ler o qr code uma vez


driver.get("https://web.whatsapp.com")

# Aguarda 2 segundos para o WhatsApp carregar
time.sleep(2)

# O programa ficará esperando que você pressione Enter
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador depois que o Enter for pressionado
driver.quit()
