from celery_factory import app

from main import get_tweets


@app.task(name='get_tweets_twitter_account_task')
def get_tweets_twitter_account_task(account_name, max_number_of_tweets):
    print('start task')
    get_tweets(account_name, max_number_of_tweets)
    print('end task')
