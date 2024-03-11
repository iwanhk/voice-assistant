from langchain_community.llms import Ollama
import base64
from PIL import Image
import io

def convert_to_base64(pil_image):
    # Convert RGBA image to RGB
    if pil_image.mode == 'RGBA':
        pil_image = pil_image.convert('RGB')

    # Save the image to a buffer
    buffered = io.BytesIO()
    pil_image.save(buffered, format="JPEG")  # Save as JPEG
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return image_base64

# def convert_to_base64(pil_image):
#     """
#     Convert PIL images to Base64 encoded strings

#     :param pil_image: PIL image
#     :return: Re-sized Base64 string
#     """

#     buffered = BytesIO()
#     pil_image.save(buffered, format="JPEG")  # You can change the format if needed
#     img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
#     return img_str


def plt_img_base64(img_base64):
    """
    Display base64 encoded string as image

    :param img_base64:  Base64 string
    """
    # Create an HTML img tag with the base64 string as the source
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'
    # Display the image by rendering the HTML
    display(HTML(image_html))

bakllava = Ollama(model="bakllava")
file_path = "text.jpg"

pil_image = Image.open(file_path)
image_b64 = convert_to_base64(pil_image)
llm_with_image_context = bakllava.bind(images=[image_b64])
llm_with_image_context.invoke("What is the code inside the picture?: ")