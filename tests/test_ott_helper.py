from unittest import TestCase
from helpers.ott_helper import get_ott_negative_deceptive, get_ott_negative_truthful
from helpers.ott_helper import get_ott_positive_deceptive, get_ott_positive_truthful


class Test(TestCase):
    def test_get_ott_negative_deceptive(self):
        dataset = get_ott_negative_deceptive()
        deceptive_unique = set(dataset['deceptive'])
        sentiment_unique = set(dataset['polarity'])

        self.assertTrue(deceptive_unique == {'deceptive'} and sentiment_unique == {'negative'})

    def test_get_ott_negative_truthful(self):
        dataset = get_ott_negative_truthful()
        deceptive_unique = set(dataset['deceptive'])
        sentiment_unique = set(dataset['polarity'])

        self.assertTrue(deceptive_unique == {'truthful'} and sentiment_unique == {'negative'})

    def test_get_ott_positive_deceptive(self):
        dataset = get_ott_positive_deceptive()
        deceptive_unique = set(dataset['deceptive'])
        sentiment_unique = set(dataset['polarity'])

        self.assertTrue(deceptive_unique == {'deceptive'} and sentiment_unique == {'positive'})

    def test_get_ott_positive_trutfhful(self):
        dataset = get_ott_positive_truthful()
        deceptive_unique = set(dataset['deceptive'])
        sentiment_unique = set(dataset['polarity'])

        self.assertTrue(deceptive_unique == {'truthful'} and sentiment_unique == {'positive'})
