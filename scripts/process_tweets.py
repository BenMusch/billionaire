import json
import re
import sys

HASHTAG_REGEX = r"#\w*[0-9a-zA-Z]+\w*[0-9a-zA-Z]\s?"
USERNAME = sys.argv[1]

def should_process(tweet):
    if tweet['is_reply_to']: return False
    if tweet['screen_name'] != USERNAME: return False

    return True

if __name__ == '__main__':
    path = 'data/tweets_%s.json' % USERNAME 
    with open(path) as f:
        data = json.load(f)
    data = filter(should_process, data)
    final_tweets = []
    for tweet in data:
        text = tweet['text'].replace("\n", "")
        no_hashtags = re.sub(HASHTAG_REGEX, '', text)
        final_tweets.insert(-1, no_hashtags)
    with open("data/tweets.txt", "a") as f:
        f.write("\n".join(final_tweets))
