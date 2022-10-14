from twython import Twython
from twython import TwythonStreamer
import configparser


class MyStreamer(TwythonStreamer):
    # Overwriting function
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet_id = data['id']
            # Liking the tweet found
            st.create_favorite(id=tweet_id)
            # Retweeting the tweet with msg
            st.update_status(status=f'Nice Tweet @{username}', in_reply_to_status_id=tweet_id)
            print(f"https://twitter.com/{username}/status/{str(tweet_id)}")


config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['keys']['api_key']
api_secret_key = config['keys']['api_secret_key']
access_token = config['keys']['access_token']
access_secret_token = config['keys']['access_secret_token']

api = MyStreamer(api_key, api_secret_key, access_token, access_secret_token)
st = Twython(api_key, api_secret_key, access_token, access_secret_token)
keyword = input("Enter keyword to track: ")
api.statuses.filter(track=keyword)
