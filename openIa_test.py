import os
from openai import OpenAI
from dotenv import load_dotenv


# Supondo que você tenha a resposta armazenada
chat_completion = {
    'id': 'chatcmpl-Aile6oKHgVrgHdh5JN9riQ9tAXoWd',
    'choices': [{
        'finish_reason': 'stop',
        'index': 0,
        'logprobs': None,
        'message': {
            'content': 'This is a test.',
            'role': 'assistant',
            'audio': None,
            'function_call': None,
            'tool_calls': None
        },
    }],
    'created': 1735232946,
    'model': 'gpt-3.5-turbo-0125',
    'object': 'chat.completion',
    'usage': {
        'completion_tokens': 6,
        'prompt_tokens': 12,
        'total_tokens': 18,
        'completion_tokens_details': {
            'accepted_prediction_tokens': 0,
            'audio_tokens': 0,
            'reasoning_tokens': 0,
            'rejected_prediction_tokens': 0
        },
        'prompt_tokens_details': {
            'audio_tokens': 0,
            'cached_tokens': 0
        }
    }
}

# Exibe a resposta gerada
print(chat_completion)

# Acessando o conteúdo
content = chat_completion['choices'][0]['message']['content']

# Exibindo o conteúdo
print(content)  # Isso exibirá "This is a test."


