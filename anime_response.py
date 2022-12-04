from dataclasses import dataclass, field 
import json

@dataclass
class AnimeResponse:
    code: int
    msg: str
    images: list = ""
    faces: list = ""
    extra: list[str] = field(default_factory=list)
    videos: list = ""

    def __post_init__(self):
        if self.code != 2114:
            self.extra = json.loads(self.extra)["img_urls"]
            #self.image_urls = json.loads(self.extra)["img_urls"]

success_data = {
  "code": 0,
  "msg": "",
  "images": [],
  "faces": [],
  "extra": "{\"img_urls\": [\"https://activity.tu.qq.com/mqq/ai_painting_anime/share/2ff21130-739e-11ed-b6ea-525400dbb5e6.jpg\", \"https://activity.tu.qq.com/mqq/ai_painting_anime/share/2ff21130-739e-11ed-b6ea-525400dbb5e6.jpg\", \"https://activity.tu.qq.com/mqq/ai_painting_anime/share/2ff21130-739e-11ed-b6ea-525400dbb5e6.jpg\", \"https://activity.tu.qq.com/mqq/ai_painting_anime/share/2ff21130-739e-11ed-b6ea-525400dbb5e6.jpg\"], \"uuid\": \"2ff21130-739e-11ed-b6ea-525400dbb5e6\"}",
  "videos": []
}

failure_data = {
  "code": 2114,
  "msg": "IMG_ILLEGAL"
}

if __name__ == "__main__":
    res = AnimeResponse(**success_data)
    print(res)
    #print(res.image_urls)
    #print(res)
    #img_urls = json.loads(res.extra)["img_urls"]

