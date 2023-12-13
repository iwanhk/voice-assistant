# 语音助手

一个简单的 Python 脚本，可以通过语音与本地大语言模型进行对话。本项目中 whisper 实现来自 mlx [官方示例库](https://github.com/ml-explore/mlx-examples/tree/main/whisper)。

### macOS 安装指南

以下为 macOS 的安装过程，Windows 与 Linux 可以使用 speech_recognition 与 pyttsx3 来替代 macOS 的 say 指令与基于 mlx 的 whisper。

#### 创建环境

```
conda create -n VoiceAI python=3.11
conda activate VoiceAI
pip install -r requirements.txt
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

# 安装音频处理工具
brew install portaudio
pip install pyaudio
```

#### 模型文件
模型文件存放于  `models/` 文件夹下，在脚本中通过变量 `MODEL_PATH` 指定。
推荐下载 TheBloke 与 XeIaso 的 gguf 格式模型，其中 6B 模型显存占用更小：
- [TheBloke/Yi-34B-Chat-GGUF](https://huggingface.co/TheBloke/Yi-34B-Chat-GGUF/blob/main/yi-34b-chat.Q8_0.gguf)
- [XeIaso/Yi-6B-Chat-GGUF](https://huggingface.co/XeIaso/yi-chat-6B-GGUF/blob/main/yi-chat-6b.Q8_0.gguf)
