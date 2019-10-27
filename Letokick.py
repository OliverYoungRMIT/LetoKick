import tweepy
from time import sleep

from SuperSecret import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


while True:
    pic = api.media_upload("/home/oliver/LetoKick/LetoKick.gif")
    api.update_status(status = "@JaredLeto", media_ids = [pic.media_id_string])
    sleep(21600)
