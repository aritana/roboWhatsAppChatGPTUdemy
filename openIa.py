import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("config.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Qual o nome do primeiro presidente do Brasil?",
        }
    ],
    #model="gpt-4",
    model="gpt-3.5-turbo"
)

# Acessando o conteúdo
content = content = chat_completion.choices[0].message.content

# Exibindo o conteúdo
print(content)  # Isso exibirá "This is a test."
