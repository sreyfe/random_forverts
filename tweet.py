import tweepy

auth = tweepy.OAuthHandler("PJnh83QnsZoFrPY2I3Yc8s3iz", "Lk2YiVhkBZMyY1PW8aM8E9A6Tp9NDHZsYV9LXhlLuMIWaJaPIa")
auth.set_access_token("1471244735536939014-EGPHlYwCxs8Z6eh0TlwD97iO6YCEXO", "Z0dPZTURFCd06AU2pnl7WvEaNQPIJKNGCB5DKAHpFXmWk")
api = tweepy.API(auth, )
status = "our very first status from python and tweepy :)"
api.update_status(status)