def load(framework):
    if framework == 'Ollama':
        from langchain_community.llms import Ollama
        return Ollama(temperature=0.0, model="gemma:2b")
    if framework == 'Tongyi':
        from langchain_community.llms import Tongyi
        from langchain_community.chat_models.tongyi import ChatTongyi
        return ChatTongyi(amodel="qwen-72b-chat")
    return None