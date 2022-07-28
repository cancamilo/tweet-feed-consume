import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

class IDPrinter(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.id)

    def on_data(self, data):
        print(data)

    def on_closed(self, error):
        print("stream closed", error)

    def on_connection_error(self):
        print("connectin error")
        self.disconnect()

token = os.environ["BEARER_TOKEN"]

streaming_client = IDPrinter(token)
streaming_client.add_rules(tweepy.StreamRule("Bitcoin"))
streaming_client.filter()

if __name__ == "__main__":
    print("hey")
    