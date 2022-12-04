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
