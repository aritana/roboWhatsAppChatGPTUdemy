import openai
from dotenv import load_dotenv

load_dotenv()

# Configure sua chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Faça a solicitação de um completion
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Explique como usar o OpenAI API corretamente."}
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Exibe a resposta gerada
print(response["choices"][0]["message"]["content"])