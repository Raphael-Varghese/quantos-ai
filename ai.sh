#!/bin/bash
export PATH="$HOME/.local/bin:$PATH"
sudo apt update && sudo apt install -y curl git
curl -LsSf https://hf.co/cli/install.sh | bash
source ~/.bashrc
sudo apt install python3.12-venv
AVAIL_RAM=$(free -g | awk '/^Mem:/{print $7}')
if [ -z "$AVAIL_RAM" ] || [ "$AVAIL_RAM" -eq 0 ]; then
    AVAIL_RAM=$(free -g | awk '/^Mem:/{print $4}')
fi
echo "Detected available RAM: ${AVAIL_RAM}GB"
if [ "$AVAIL_RAM" -ge 28 ]; then
    MODEL_REPO="unsloth/Qwen3.5-32B-GGUF"
    MODEL_FILE="Qwen3.5-32B-Q4_K_M.gguf"
elif [ "$AVAIL_RAM" -ge 16 ]; then
    MODEL_REPO="bartowski/Qwen_Qwen3.5-9B-GGUF"
    MODEL_FILE="Qwen3.5-24B-Q4_K_M.gguf"
elif [ "$AVAIL_RAM" -ge 14 ]; then
    MODEL_REPO="unsloth/Qwen3.5-14B-GGUF"
    MODEL_FILE="Qwen3.5-14B-Q4_K_M.gguf"
elif [ "$AVAil_RAM" -ge 8 ]; then
    MODEL_REPO="unsloth/Qwen3.5-7B-GGUF"
    MODEL_FILE="Qwen3.5-7B-Q4_K_M.gguf"
elif [ "$AVAIL_RAM" -ge 4 ]; then
    MODEL_REPO="unsloth/Qwen3.5-3B-GGUF"
    MODEL_FILE="Qwen3.5-3B-Q4_K_M.gguf"
else
    MODEL_REPO="unsloth/Qwen3.5-0.8B-GGUF"
    MODEL_FILE="Qwen3.5-0.8B-Q4_K_M.gguf"
fi
echo "Chosen model repository: $MODEL_REPO"
echo "Chosen model file: $MODEL_FILE"
python3 -m venv ai-env
source ai-env/bin/activate
hf download "$MODEL_REPO" "$MODEL_FILE" --local-dir . && mv "$MODEL_FILE" model.gguf
python3 -m pip install diskcache typing-extensions numpy requests beautifulsoup4
python3 -m pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
python3 main.py
