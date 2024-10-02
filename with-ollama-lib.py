import ollama
from config import *


def main():
    prompt = 'write a 2000 words story'

    # Call the model with streaming enabled
    for response in ollama.generate(
        model='qwen:0.5b',
        prompt=prompt,
        stream=ollama_stream,
    ):
        if 'response' in response:
            print(response['response'], end='', flush=True)

    print()


if __name__ == '__main__':
    main()
