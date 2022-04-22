import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

api_key = os.getenv('API_KEY')
endpoint = os.getenv('ENDPOINT')

credential = AzureKeyCredential(api_key)
text_analytics_client = TextAnalyticsClient(endpoint, credential)


def get_overall_sentiment(phrase):
    documents = [phrase]
    response = text_analytics_client.analyze_sentiment(documents, language='en')
    result = response[0]
    if result.is_error:
        raise ValueError(
            "Sentiment analysis of document failed with code '{}' and message '{}'".format(result.error.code,
                                                                                           result.error.message))

    positive = result.confidence_scores.positive
    neutral = result.confidence_scores.neutral
    negative = result.confidence_scores.negative

    return positive, neutral, negative

