from math import ceil


def sentiment_to_opencv(overall_sentiment):
    positive, neutral, negative = overall_sentiment
    blue = ceil(neutral*255)
    green = ceil(positive*255)
    red = ceil(negative * 255)

    return blue, green, red
