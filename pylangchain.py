
import sys
import os
from langchain_community.llms import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain.schema import HumanMessage, SystemMessage, AIMessage


if __name__ == "__main__":


    key=os.getenv('DASHSCOPE_API_KEY', '')

    chat = ChatTongyi(amodel="qwen-72b-chat", app_key=key)

    ret= chat.invoke(
        [
            SystemMessage(content="You are a nice AI bot that helps a user figure out where to travel in one short sentence"),
            HumanMessage(content="I like the beaches where should I go?"),
            AIMessage(content="You should go to Nice, France"),
            HumanMessage(content="What else should I do when I'm there?")
        ]
    )

    print(f"{type(ret)}, {ret}")
