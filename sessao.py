from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os 

# Definir o caminho do binário do Chrome
options = Options()
options.binary_location = '/usr/bin/google-chrome'  # Caminho correto do Chrome no seu sistema

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
time.sleep(2)

# O programa ficará esperando que você pressione Enter
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador depois que o Enter for pressionado
driver.quit()
