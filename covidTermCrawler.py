from credentials import *
import tweepy
import time
from pandas import DataFrame

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

text_query = "covid" or "corona" or "sars" or "pandemia"
count = 10000
lang = "pt-br"
try:
  # Query com os parametros
  tweets = tweepy.Cursor(
    api.search,
    q=text_query,
    lang=lang,
    tweet_mode="extended",
    ).items(count)

  all_tweets = []

  for tweet in tweets:
    # Filtrar se não é retweet
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
  
      all_tweets.append(tweet)
      print('Numero de Tweets baixados até agora: {}'.format(len(all_tweets)))

      outtweets = [[tweet.id_str, 
                tweet.created_at, 
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8")] 
              for idx,tweet in enumerate(all_tweets)]
      df = DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count", "text"])
      df.to_csv('covidVariationsTermCrawler_tweets.csv',index=False)
      df.head(3)
 
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)