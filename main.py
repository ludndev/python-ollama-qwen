import json
import requests
from config import *


def main():
    prompt = 'Tell me a joke about programmer'

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'model': 'qwen:0.5b',
        'prompt': prompt,
        'stream': ollama_stream,
    }

    response = requests.post(ollama_api, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        answers = data['response']
        print(answers)
    else:
        print('Something went wrong. Error:',  response.status_code, response.text)


if __name__ == '__main__':
    main()
