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


if __name__ == '__main__':
    main()
