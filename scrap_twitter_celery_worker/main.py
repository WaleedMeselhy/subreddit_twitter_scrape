import GetOldTweets3 as got
import os
from elasticsearch import Elasticsearch

es = Elasticsearch([os.environ['ELASTICSEARCH_HOST']])


def get_tweets(account_name, max_number_of_tweets=2000):
    tweet_criteria = got.manager.TweetCriteria().setUsername(
        account_name).setMaxTweets(max_number_of_tweets)

    tweets = got.manager.TweetManager.getTweets(tweet_criteria)
    for tweet in tweets:
        e1 = {"tweet": tweet.text}

        res = es.index(index='twitter', doc_type='tweet', body=e1)
        print(res)