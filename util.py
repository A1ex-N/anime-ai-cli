import requests
import base64


def image_to_base64(filename: str) -> str:
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')


def save_anime_image(output_name: str, image_url: str):
    image_bytes = requests.get(image_url).content
    with open(output_name, "wb") as img:
        img.write(image_bytes)
    print("Saved processed image to ", output_name)