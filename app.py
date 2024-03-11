from base64 import b64encode
from PIL import Image
import sys
from io import BytesIO
from langchain_community.llms import Ollama

def toBase64(image_path):
    with open(image_path, "rb") as f:
        encoded_image = b64encode(f.read()).decode("utf-8")
        return 'Hi! What is in this image? <img src=\"data:image/png;base64,'+encoded_image+'" />' 

def putchar(c):
    sys.stdout.write(c) 
    sys.stdout.flush() 

def strip(content):
    # this is the content of the response
    # 'data: {"id":"35b1c0d3-2333-4d7c-98bb-53792beffb98","choices":[{"index":0,"delta":{"role":"assistant","content":"I"},"finish_reason":null}]}'
    if content.split(' ')[0]!= 'data:':
        return ""
    try:
        c= content.split('content":"')[1].split('"')[0]
        # replace \n with \n
        c= c.replace('\\n', '\n')
        return c
    except:
        # print(content)
        return ""

def process(query):
    llm = Ollama(model="gemma:2b")

    for chunks in llm.stream(query):
        putchar(chunks)
    print('\n')

if __name__ == "__main__":
    if len(sys.argv) == 2:  
        process(sys.argv[1])
        sys.exit(0)
    print("Usage: python app.py <query>")
    sys.exit(1)