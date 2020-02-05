from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API, Cursor
import csv

import cred


class StdOutListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    auth = OAuthHandler(cred.API_KEY, cred.API_KEY_SECRET)
    auth.set_access_token(cred.ACCESS_TOKEN, cred.ACCESS_TOKEN_SECRET)

    api = API(auth, wait_on_rate_limit=True)

    # Open/Create a file to append data
    csvFile = open('ua.csv', 'a')
    writer = csv.DictWriter(csvFile, fieldnames=["Date", "Text"])
    writer.writeheader()
    # Use csv Writer
    csvWriter = csv.writer(csvFile)

    for tweet in Cursor(api.search, q="MPUR", count=100,
                        lang="en",
                        since="2017-04-03").items():
        print(tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
