import pandas as pd

from helpers.visual_helper import phrase_to_pixel, generate_image
from helpers.ott_helper import get_ott_negative_deceptive, get_ott_negative_truthful
from helpers.ott_helper import get_ott_negative_deceptive_colored


def run_deceptive_negative():
    negative_deceptive = get_ott_negative_deceptive()
    negative_deceptive['sentiment'] = negative_deceptive['text'].apply(lambda x: phrase_to_pixel(x, show_status=True))
    negative_deceptive.to_csv('local_datasets/deceptive_negative_colored.csv', index=False)


def run_truthful_negative():
    negative_truthful = get_ott_negative_truthful()
    negative_truthful['sentiment'] = negative_truthful['text'].apply(lambda x: phrase_to_pixel(x, show_status=True))
    negative_truthful.to_csv('local_datasets/truthful_negative_colored.csv', index=False)


def colorize_deceptive_negative():
    ott_negative_deceptive_colored = get_ott_negative_deceptive_colored()
    ott_negative_deceptive_colored['sentiment'] = ott_negative_deceptive_colored['sentiment'].apply(
        lambda x: x.split(' '))
    generate_image(ott_negative_deceptive_colored['sentiment'], 'artifacts/deceptive_negative.png')


if __name__ == '__main__':
    run_truthful_negative()
