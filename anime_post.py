from anime_response import AnimeResponse
from dataclasses import dataclass
from util import image_to_base64
import requests
import json
import hashlib

# Even though images is a list, you can't actually provide more than one image.
# you get the msg "list index out of range"
@dataclass
class AnimePost:
    images: list[str]
    busiId: str = "different_dimension_me_img_entry"
    extra: str = "{\"face_rects\":[],\"version\":2,\"platform\":\"web\",\"data_report\":{\"parent_trace_id\":\"4c689320-71ba-1909-ab57-13c0804d4cc6\",\"root_channel\":\"\",\"level\":0}}"

    def __post_init__(self):
        if len(self.images) > 1:
            print("AnimePost.images can only have 1 image. Using the first image in the list")

    @staticmethod
    def get_anime_image(filename: str) -> AnimeResponse:
        post_url = "https://ai.tu.qq.com/overseas/trpc.shadow_cv.ai_processor_cgi.AIProcessorCgi/Process"
        base64_image = image_to_base64(filename)
        post_data = AnimePost(images=[base64_image])
        post_str = json.dumps(post_data.__dict__)
        url = f'https://h5.tu.qq.com{str(len(post_str))}HQ31X02e'.encode()
        sign_value = hashlib.md5(url).hexdigest()
        headers = {
        'Host': 'ai.tu.qq.com',
        "x-sign-value": sign_value, 
        "x-sign-version": "v1",
        'Origin': 'https://h5.tu.qq.com'
        }
        res = requests.post(post_url, headers=headers, json=post_data.__dict__)
        json_data = res.json()
        anime = AnimeResponse(**json_data) 
        return anime
