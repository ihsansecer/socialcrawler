import tweepy


class UserCrawler(object):
    def __init__(self, user_id, api):
        self._api = api
        self._user_id = user_id
        self._data = {}

    def _init_user(self, user_id):
        self._data.setdefault(user_id, {
            "friends": {},
            "followers": {}
        })

    def _extend_user(self, parent_id, user_id, connection_type):
        self._data[parent_id][connection_type].setdefault(user_id, {
            "friends": {},
            "followers": {}
        })

    def _fetch_connection_ids(self, user_id, connection_type):
        connection_fetcher = getattr(self._api, "{}_ids".format(connection_type))
        try:
            return tweepy.Cursor(connection_fetcher, id=user_id).items()
        except tweepy.TweepError:
            return []

    def _crawl_connections(self, connection_type, user_id, depth):
        self._init_user(user_id)
        connection_ids = self._fetch_connection_ids(user_id, connection_type)
        for connection_id in connection_ids:
            self._extend_user(user_id, connection_id, connection_type)
            if depth > 1:
                self._crawl_all(connection_id, depth - 1)

    def _crawl_friends(self, *args):
        self._crawl_connections("friends", *args)

    def _crawl_followers(self, *args):
        self._crawl_connections("followers", *args)

    def _crawl_all(self, *args):
        self._crawl_friends(*args)
        self._crawl_followers(*args)

    def crawl(self, depth=1):
        self._crawl_all(self._user_id, depth)
        return self._data


class UserTweetCrawler(object):
    def __init__(self, api, user_id):
        self._api = api
        self._user_id = user_id
        self._data = {}
        self._data.setdefault(user_id, {"tweets": {}})

    def crawl(self):
        try:
            tweets = tweepy.Cursor(self._api.user_timeline, id=self._user_id).items()
            for tweet in tweets:
                self._data[self._user_id]["tweets"]\
                    .setdefault(tweet.id_str, {"date": str(tweet.created_at), "tweet": tweet.text})
            return self._data
        except tweepy.TweepError:
            return []