from selenium import webdriver
import time

# Inicia o navegador Chrome
driver = webdriver.Chrome()

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarda 2 segundos para o WhatsApp carregar
time.sleep(2)

# O programa ficará esperando que você pressione Enter
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador depois que o Enter for pressionado
driver.quit()


