from helpers.visual_helper import phrase_to_pixel
from helpers.ott_helper import get_ott_negative_deceptive

if __name__ == '__main__':
    negative_deceptive = get_ott_negative_deceptive()
    negative_deceptive['sentiment'] = negative_deceptive['text'].apply(lambda x: phrase_to_pixel(x, show_status=True))
    negative_deceptive.to_csv('deceptive_negative_colored.csv', index=False)
