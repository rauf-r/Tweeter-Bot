import tweepy
import time

consumer_key = 'consumer_key here'
consumer_secret = 'consumer_secret key here'
access_token = 'access_token key here'
access_token_secret = 'access_token_secret key here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
# print(user)     # it gives all the details, like name, screen name, location, and various other info.
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "bitcoin"
numberOfTweets = 2

def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
            
        except tweepy.RateLimitError:
            print("Sleeping now....")
            time.sleep(10)    # sleeps for 10 secs


# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     if follower.name == 'Usernamehere':
#         print(follower.name)
#         follower.follow()


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
