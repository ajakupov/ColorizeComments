from unittest import TestCase
from helpers.visual_helper import sentiment_to_opencv

class Test(TestCase):
    def test_sentiment_to_opencv_positive(self):
        overal_sentiment = 1.0, 0.0, 0.0
        blue, green, red = sentiment_to_opencv(overal_sentiment)
        self.assertTrue(blue == 0 and red == 0 and green == 255)

    def test_sentiment_to_opencv_negative(self):
        overal_sentiment = 0.0, 0.0, 1.0
        blue, green, red = sentiment_to_opencv(overal_sentiment)
        self.assertTrue(blue == 0 and red == 255 and green == 0)

    def test_sentiment_to_opencv_neutral(self):
        overal_sentiment = 0.0, 1.0, 0.0
        blue, green, red = sentiment_to_opencv(overal_sentiment)
        self.assertTrue(blue == 255 and red == 0 and green == 0)

    def test_sentiment_to_opencv_mixed(self):
        overal_sentiment = 0.7, 0.2, 0.9
        blue, green, red = sentiment_to_opencv(overal_sentiment)
        self.assertTrue(blue == 51 and red == 230 and green == 179)
