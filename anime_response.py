from dataclasses import dataclass, field 
import json
from enum import Enum

class ErrorCodes(Enum):
    SUCCESS = 0
    NUDITY = 2114
    NO_FACE = 1001
    AUTH_FAILED = -2111
    USER_IP_COUNTRY = 2119
    PARAM_INVALID = -2100
    CONNECTION_CLOSED = 141


@dataclass
class AnimeResponse:
    code: int
    msg: str
    images: list = ""
    faces: list = ""
    extra: list[str] = field(default_factory=list)
    videos: list = ""

    def __post_init__(self):
        success = False

        match ErrorCodes(self.code):
            case ErrorCodes.AUTH_FAILED:
                print("Auth failed. Don't know how to solve this one.")
            case ErrorCodes.NUDITY:
                print("Image rejected. Nudity isn't allowed.")
            case ErrorCodes.NO_FACE:
                print("No face in image. Can't process.")
            case ErrorCodes.USER_IP_COUNTRY:
                print("Your ip is not from china, try using vpn or proxies.")
            case ErrorCodes.PARAM_INVALID:
                print("Invalid file format. Must be one of jpeg|gif|png|bmp|ico|svg|tiff|ai|drw|pct|psp|xcf|psd|raw|webp.")
            case ErrorCodes.CONNECTION_CLOSED:
                print("The connection was forcibly closed by the host. (Is the image too big?)")
            case ErrorCodes.SUCCESS:
                self.extra = json.loads(self.extra)["img_urls"]
                success = True

        if not success:
            exit(1)
