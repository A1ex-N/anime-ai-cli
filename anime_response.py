from dataclasses import dataclass, field 
import json


ERROR_CODE_NUDITY = 2114
ERROR_CODE_NO_FACE = 1001
ERROR_CODE_AUTH_FAILED = -2111
ERROR_CODE_USER_IP_COUNTRY = 2119


@dataclass
class AnimeResponse:
    code: int
    msg: str
    images: list = ""
    faces: list = ""
    extra: list[str] = field(default_factory=list)
    videos: list = ""

    def __post_init__(self):
        if self.code == ERROR_CODE_AUTH_FAILED:
            print("Auth failed. Don't know how to solve this one")
            exit(1)
        if self.code == ERROR_CODE_NUDITY:
            print("Image rejected. Nudity isn't allowed.")
            exit(1)
        if self.code == ERROR_CODE_NO_FACE:
            print("No face in image. Can't process")
            exit(1)
        if self.code == ERROR_CODE_USER_IP_COUNTRY:
            print("Your ip is not from china, try using vpn or proxies.")
            exit(1)

        self.extra = json.loads(self.extra)["img_urls"]
