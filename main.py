import pandas as pd

from helpers.visual_helper import phrase_to_pixel, generate_image, mix_colors
from helpers.ott_helper import get_ott_negative_deceptive, get_ott_negative_truthful
from helpers.ott_helper import get_ott_positive_deceptive, get_ott_positive_truthful
from helpers.ott_helper import get_ott_negative_deceptive_colored, get_ott_negative_truthful_colored
from helpers.ott_helper import get_ott_positive_deceptive_colored, get_ott_positive_truthful_colored


def run_deceptive_negative():
    negative_deceptive = get_ott_negative_deceptive()
    negative_deceptive['sentiment'] = negative_deceptive['text'].apply(lambda x: phrase_to_pixel(x, show_status=True))
    negative_deceptive.to_csv('local_datasets/deceptive_negative_colored.csv', index=False)


def run_truthful_negative():
    negative_truthful = get_ott_negative_truthful()
    negative_truthful['sentiment'] = negative_truthful['text'].apply(lambda x: phrase_to_pixel(x, show_status=True))
    negative_truthful.to_csv('local_datasets/truthful_negative_colored.csv', index=False)


def run_deceptive_positive():
    positive_deceptive = get_ott_positive_deceptive()
    positive_deceptive['sentiment'] = positive_deceptive['text'].apply(lambda x: phrase_to_pixel(x, show_status=True))
    positive_deceptive.to_csv('local_datasets/deceptive_positive_colored.csv', index=False)


def run_truthful_positive():
    positive_truthful = get_ott_positive_truthful()
    positive_truthful['sentiment'] = positive_truthful['text'].apply(lambda x: phrase_to_pixel(x, show_status=True))
    positive_truthful.to_csv('local_datasets/truthful_positive_colored.csv', index=False)


def colorize_deceptive_negative():
    ott_negative_deceptive_colored = get_ott_negative_deceptive_colored()
    ott_negative_deceptive_colored['sentiment'] = ott_negative_deceptive_colored['sentiment'].apply(
        lambda x: x.split(' '))
    generate_image(ott_negative_deceptive_colored['sentiment'], 'artifacts/deceptive_negative.png')


def colorize_deceptive_positive():
    ott_positive_deceptive_colored = get_ott_positive_deceptive_colored()
    ott_positive_deceptive_colored['sentiment'] = ott_positive_deceptive_colored['sentiment'].apply(
        lambda x: x.split(' '))
    generate_image(ott_positive_deceptive_colored['sentiment'], 'artifacts/deceptive_positive.png')


def colorize_truthful_negative():
    ott_negative_truthful_colored = get_ott_negative_truthful_colored()
    ott_negative_truthful_colored['sentiment'] = ott_negative_truthful_colored['sentiment'].apply(
        lambda x: x.split(' '))
    generate_image(ott_negative_truthful_colored['sentiment'], 'artifacts/truthful_negative.png')


def colorize_truthful_positive():
    ott_positive_truthful_colored = get_ott_positive_truthful_colored()
    ott_positive_truthful_colored['sentiment'] = ott_positive_truthful_colored['sentiment'].apply(
        lambda x: x.split(' '))
    generate_image(ott_positive_truthful_colored['sentiment'], 'artifacts/truthful_positive.png')


def colorize_deceptive_negative_average():
    ott_negative_deceptive_colored = get_ott_negative_deceptive_colored()
    ott_negative_deceptive_colored['sentiment'] = ott_negative_deceptive_colored['sentiment'].apply(
        lambda x: x.split(' '))
    mix_colors(ott_negative_deceptive_colored['sentiment'], 'artifacts/deceptive_negative_average.png')


def colorize_deceptive_positive_average():
    ott_positive_deceptive_colored = get_ott_positive_deceptive_colored()
    ott_positive_deceptive_colored['sentiment'] = ott_positive_deceptive_colored['sentiment'].apply(
        lambda x: x.split(' '))
    mix_colors(ott_positive_deceptive_colored['sentiment'], 'artifacts/deceptive_positive_average.png')


def colorize_truthful_negative_average():
    ott_negative_truthful_colored = get_ott_negative_truthful_colored()
    ott_negative_truthful_colored['sentiment'] = ott_negative_truthful_colored['sentiment'].apply(
        lambda x: x.split(' '))
    mix_colors(ott_negative_truthful_colored['sentiment'], 'artifacts/truthful_negative_average.png')


def colorize_truthful_positive_average():
    ott_positive_truthful_colored = get_ott_positive_truthful_colored()
    ott_positive_truthful_colored['sentiment'] = ott_positive_truthful_colored['sentiment'].apply(
        lambda x: x.split(' '))
    mix_colors(ott_positive_truthful_colored['sentiment'], 'artifacts/truthful_positive_average.png')


if __name__ == '__main__':
    colorize_deceptive_negative_average()
    colorize_deceptive_positive_average()
    colorize_truthful_negative_average()
    colorize_truthful_positive_average()
