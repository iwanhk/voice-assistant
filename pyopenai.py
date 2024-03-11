from langchain_openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

llm.predict("hi!")

chat_model.predict("hi!")