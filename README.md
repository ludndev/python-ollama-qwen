# python-ollama-qwen

This project demonstrates how to interact with the `qwen:0.5b` model using the `ollama` library in Python. It provides examples of how to run the model using both raw HTTP requests and the official `ollama` Python library.

## Prerequisites

- [Ollama](https://ollama.com) installed on your system.

To install Ollama, run the following command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Setup

1. Pull the `qwen:0.5b` model:
   ```bash
   ollama pull qwen:0.5b
   ```
   
2. Start ollama server:
   ```bash
   ollama serve
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Examples

Run the example with raw HTTP requests:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License.
