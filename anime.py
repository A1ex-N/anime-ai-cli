from util import save_anime_image
from anime_post import AnimePost
import random
import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide a filename")
        exit(1)

    output_name = ''.join(random.choices(ALPHABET, k=6)) + ".jpg"

    if len(sys.argv) == 3:
        output_name = sys.argv[2]

    filename = sys.argv[1]
    print("Processing image: ", filename)
    anime = AnimePost.get_anime_image(filename)
    save_anime_image(output_name, anime.extra[0])
