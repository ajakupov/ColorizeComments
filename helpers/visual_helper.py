import cv2
import numpy as np
from math import ceil
from helpers.cognitive_helper import get_overall_sentiment


def phrase_to_pixel(phrase, show_status=False):
    blue, green, red = sentiment_to_opencv(get_overall_sentiment(phrase))

    if show_status:
        print("processed")
    return "{} {} {}".format(blue, green, red)


def sentiment_to_opencv(overall_sentiment):
    positive, neutral, negative = overall_sentiment
    blue = ceil(neutral*255)
    green = ceil(positive*255)
    red = ceil(negative * 255)

    return blue, green, red


def generate_image(reviews_bgr, image_name):
    if len(reviews_bgr) != 400:
        return False
    image = np.zeros((20, 20, 3), dtype=np.uint8)
    counter = 0
    for i in range(20):
        for j in range(20):
            image[i][j] = reviews_bgr[counter]
            counter += 1
    return cv2.imwrite(image_name, image)


def mix_colors(reviews_bgr, image_name):
    average_blue = 0
    average_green = 0
    average_red = 0
    for blue, green, red in reviews_bgr:
        average_blue += int(blue)
        average_green += int(green)
        average_red += int(red)

    average_blue = ceil(average_blue/len(reviews_bgr))
    average_green = ceil(average_green / len(reviews_bgr))
    average_red = ceil(average_red / len(reviews_bgr))
    image = np.zeros((150, 150, 3), dtype=np.uint8)
    image[:] = (average_blue, average_green, average_red)

    return cv2.imwrite(image_name, image)
