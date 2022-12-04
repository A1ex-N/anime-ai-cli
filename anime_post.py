from anime_response import AnimeResponse
from dataclasses import dataclass
from util import image_to_base64
import requests


# Even though images is a list, you can't actually provide more than one image.
# you get the msg "list index out of range"
@dataclass
class AnimePost:
    images: list[str]
    busiId: str = "ai_painting_anime_img_entry"
    extra: str = "{\"face_rects\":[],\"version\":2,\"platform\":\"web\",\"data_report\":{\"parent_trace_id\":\"4c689320-71ba-1909-ab57-13c0804d4cc6\",\"root_channel\":\"\",\"level\":0}}"


    def __post_init__(self):
        if len(self.images) > 1:
            print("AnimePost.images can only have 1 image. Using the first image in the list")


    @staticmethod
    def get_anime_image(filename: str) -> AnimeResponse:
        post_url = "https://ai.tu.qq.com/trpc.shadow_cv.ai_processor_cgi.AIProcessorCgi/Process"
        base64_image = image_to_base64(filename)
        post_data = AnimePost(images=[base64_image])
        res = requests.post(post_url, json=post_data.__dict__)
        json_data = res.json()
        anime = AnimeResponse(**json_data) 
        if anime.code == 2114:
            print("Image rejected. Nudity isn't allowed.")
            exit(1)
        return anime
