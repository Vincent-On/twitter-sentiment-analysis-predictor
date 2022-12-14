"""
Object to manage collection of tweets.
"""
import pandas as pd

from nltk.tokenize import TweetTokenizer


class TweeterCollection:
    """
    Represents a collection of tweets and users.
    """
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.tweets = self.get_all_tweets()

    def get_all_tweets(self):
        """
        Get all tweets from the collection in a single array.

        :return: list, contains the content of all tweets in the collection
        """
        return self.data["Content"].tolist()

    def get_all_tweets_tokenized(self):
        """
        Return all tweets tokenized.

        Strips all handles (mentions) from tweets as well.

        :return: list, containing all words in all tweets
        """
        toknizer = TweetTokenizer(strip_handles=True, reduce_len=True)
        input_tweets = self.get_all_tweets()
        output_tweets = []
        for tweet in input_tweets:
            tweet = toknizer.tokenize(tweet)
            for token in tweet:
                output_tweets.append(token)
        return output_tweets

    def get_data(self):
        """
        Get the dataset

        :return: pd.Dataframe
        """
        return self.data
