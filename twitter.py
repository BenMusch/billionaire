import os
import random
import logging

import tweepy
from textgenrnn import textgenrnn

logging.basicConfig(level=logging.INFO)

consumer_key = os.environ["CONSUMER_API_KEY"]
consumer_secret = os.environ["CONSUMER_API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

textgen = textgenrnn('textgenrnn_weights.hdf5')
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

def gen_tweet():
    try:
        return textgen.generate(
                temperature=random.uniform(0.5, 1.001),
                return_as_list=True
        )[0]
    except Exception as e:
        logging.exception(e)
        return ['_' * 300] # dumb hack to force re-generation

def get_tweet_text():
    text = gen_tweet()
    while len(text) > 280: text = gen_tweet()
    return text

def do_tweet(*args):
    text = get_tweet_text()
    logging.info('trying to tweet "%s" (len %s)' % (text, len(text)))
    api.update_with_media('img/' + random.choice(os.listdir('img/')), status=text)

if __name__ == '__main__':
    do_tweet()
