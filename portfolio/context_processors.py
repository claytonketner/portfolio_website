import random
from .constants import SUBTITLES


def subtitles(request):
    random_index = random.randint(0, len(SUBTITLES)-1)
    return {'subtitle': SUBTITLES[random_index]}
