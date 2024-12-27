from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os 
import signal
from openai import OpenAI
from dotenv import load_dotenv


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

# Aguarda x segundos para o WhatsApp carregar
driver.implicitly_wait(10)

#sair do loop
def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!')
    print('Exiting gracefully...')
    driver.quit()
    exit(0)


def sends_message_to_user(message):
    # Localize a div com contenteditable="true", role="textbox" e placeholder contendo "mensagem"
    div_element = driver.find_element(
        By.XPATH, '//div[contains(@aria-placeholder, "mensagem")]'
    )

    # Simular digitação para substituir o <br> por <span>
    div_element.send_keys(message)
    driver.implicitly_wait(0.5)        
    div_element.send_keys(Keys.ENTER)    
    return     

def openAI(user_message):
    load_dotenv("config.env")
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_message
        }
    ],
    #model="gpt-4",
    model="gpt-3.5-turbo"
    )
    # Acessando o conteúdo
    content = chat_completion.choices[0].message.content
    # Exibindo o conteúdo
    print(content)  # Isso exibirá "This is a test."
    sends_message_to_user(content)
    return

#capturar Notificação
def bot():
    try: 
        elements = driver.find_elements(By.XPATH, "//*[contains(@aria-label, 'mensage') and contains(@aria-label, 'não lida')]")

        #elements = driver.find_elements(By.CLASS_NAME, "x7h3shv")      

        if elements:         
            selectedElement =  elements[-1]
            action = webdriver.common.action_chains.ActionChains(driver)    
            action.move_to_element_with_offset(selectedElement, 0, -20).double_click().perform() 

             # Espera um pouco para a mensagem ser carregada
            driver.implicitly_wait(10)
            
            # Capturar a última mensagem na conversa
            messages = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text")
            
            if messages:
                # Localizar o <span> filho com a classe vazia e pegar o texto
                last_message_span = messages[-1].find_element(By.CSS_SELECTOR, "span[class='']")
                last_message = last_message_span.text
                print("Última mensagem recebida:", last_message)     
                openAI(last_message)     
                                            
                # Aqui você pode processar a mensagem usando IA, responder, etc.
                
        else:
            print("Nenhuma mensagem não lida encontrada.")          
        #Gets the new message

        #allMessages =  driver.find_elements()

        #Process the message on the IA api


        #Answer the message and closes the contact    
    except:
        print("buscando novas notificações")        

# Registra o sinal de interrupção
signal.signal(signal.SIGINT, signal_handler)

while True:
    bot()

# Fecha o navegador depois que o Enter for pressionado
driver.quit()
