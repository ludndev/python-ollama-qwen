import json
import requests
from config import *


def call_llm_with_stream(data, headers):
    response = requests.post(ollama_api, data=json.dumps(data), headers=headers, stream=True)

    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                chunk_data = chunk.decode('utf-8')

                try:
                    data = json.loads(chunk_data)
                    if 'response' in data:
                        print(data['response'], end='', flush=True)
                except json.JSONDecodeError:
                    # incomplete content
                    pass
        print()  # new line to separate at end of the stream
    else:
        print('Something went wrong. Error:', response.status_code, response.text)


def call_llm_default(data, headers):
    response = requests.post(ollama_api, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        response_data = json.loads(response.text)
        answers = response_data['response']
        print(answers)
    else:
        print('Something went wrong. Error:', response.status_code, response.text)


def main():
    prompt = 'write a 2000 words story'

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'model': ollama_model,
        'prompt': prompt,
        'stream': ollama_stream,
    }

    if ollama_stream:
        call_llm_with_stream(data, headers)
    else:
        call_llm_default(data, headers)


if __name__ == '__main__':
    main()
