from unittest import TestCase
from helpers.cognitive_helper import get_overall_sentiment

class Test(TestCase):
    def test_get_overall_sentiment(self):
        test_phrase = "The food was yummy. :)"
        positive, neutral, negative = get_overall_sentiment(test_phrase)
        self.assertTrue(isinstance(positive, float)
                        and isinstance(neutral, float)
                        and isinstance(negative, float))
