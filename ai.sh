#!/bin/bash
export PATH="$HOME/.local/bin:$PATH"
sudo apt update && sudo apt install -y curl git
curl -LsSf https://hf.co/cli/install.sh | bash
source ~/.bashrc
sudo apt install python3.12-venv
MODEL_REPO="bartowski/Qwen_Qwen3.5-9B-GGUF"
MODEL_FILE="Qwen3.5-9B-Q4_K_M.gguf"
echo "Chosen model repository: $MODEL_REPO"
echo "Chosen model file: $MODEL_FILE"
python3 -m venv ai-env
source ai-env/bin/activate
hf download "$MODEL_REPO" "$MODEL_FILE" --local-dir .
python3 -m pip install diskcache typing-extensions numpy requests beautifulsoup4
python3 -m pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
python3 main.py
