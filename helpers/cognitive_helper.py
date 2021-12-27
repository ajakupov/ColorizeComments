import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

api_key = os.getenv("API_KEY")
endpoint = os.getenv("ENDPOINT")

credential = AzureKeyCredential(api_key)
text_analytics_client = TextAnalyticsClient(endpoint, credential)

def get_overall_sentiment(phrase):
    documents = [phrase]
    response = text_analytics_client.analyze_sentiment(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    output = result[0]

    positive = output.confidence_scores.positive
    neutral = output.confidence_scores.neutral
    negative = output.confidence_scores.negative

    return positive, neutral, negative

