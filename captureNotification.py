from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os 


# Definir o caminho do binário do Chrome
options = Options()
options.binary_location = '/usr/bin/google-chrome'  # Caminho correto do Chrome no seu sistema
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# Definir o diretório para o perfil do usuário (ex: para o WhatsApp Web manter a sessão)
dir_path = os.getcwd()
options.add_argument(f"user-data-dir={dir_path}/profile/zap")  # Diretório do perfil

# Usar o ChromeDriverManager para gerenciar o driver
service = Service(ChromeDriverManager().install())

# Inicializa o driver com as opções definidas
driver = webdriver.Chrome(service=service, options=options)

# Acesse o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarda 2 segundos para o WhatsApp carregar
driver.implicitly_wait(10)


#capturar Notificação
def bot():
    try:
        print("try")
        elements = driver.find_elements(By.XPATH, "//*[contains(@aria-label, 'mensage') and contains(@aria-label, 'não lida')]")

        #elements = driver.find_elements(By.CLASS_NAME, "x7h3shv")      

        if elements:
            print(elements)
            selectedElement =  elements[-1]
            action = webdriver.common.action_chains.ActionChains(driver)    
            action.move_to_element_with_offset(selectedElement, 0, -20).double_click().perform() 
    except:
        print("buscando novas notificações")
try:
    while True:
        bot()
except KeyboardInterrupt:#control+c
    print("O script foi interrompido pelo usuário.")



# Fecha o navegador depois que o Enter for pressionado
driver.quit()
