import pandas as pd


def read_ott():
    """
    Either we run it from main or from inside the folder, thus the relative path changes
    """
    try:
        ott_path = '../local_datasets/deceptive-opinion.csv'
        ott_deceptive = pd.read_csv(ott_path, encoding='utf-8', sep=',', engine='python')
    except FileNotFoundError:
        ott_path = './local_datasets/deceptive-opinion.csv'
        ott_deceptive = pd.read_csv(ott_path, encoding='utf-8', sep=",", engine='python')
    return ott_deceptive


def get_ott_negative():
    ott_dataframe = read_ott()
    ott_dataframe_negative = ott_dataframe[ott_dataframe['polarity'] == 'negative']
    return ott_dataframe_negative


def get_ott_positive():
    ott_dataframe = read_ott()
    ott_dataframe_negative = ott_dataframe[ott_dataframe['polarity'] == 'positive']
    return ott_dataframe_negative


def get_ott_negative_deceptive():
    ott_dataframe_negative = get_ott_negative()
    ott_dataframe_negative_deceptive = ott_dataframe_negative[ott_dataframe_negative['deceptive'] == 'deceptive']
    return ott_dataframe_negative_deceptive


def get_ott_negative_truthful():
    ott_dataframe_negative = get_ott_negative()
    ott_dataframe_negative_truthful = ott_dataframe_negative[ott_dataframe_negative['deceptive'] == 'truthful']
    return ott_dataframe_negative_truthful


def get_ott_negative_deceptive_colored():
    try:
        path = '../local_datasets/deceptive_negative_colored.csv'
        ott_negative_deceptive_sentiment = pd.read_csv(path, encoding='utf-8', sep=',', engine='python')
    except FileNotFoundError:
        path = './local_datasets/deceptive_negative_colored.csv'
        ott_negative_deceptive_sentiment = pd.read_csv(path, encoding='utf-8', sep=",", engine='python')

    return ott_negative_deceptive_sentiment
