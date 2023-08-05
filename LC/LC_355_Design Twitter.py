## Linked List

### Date: 08/01/2023

class Twitter:

    def __init__(self):
        self.globalTime = 0
        self.idToUser = {}

    class Treet:
        def __init__(self, id:int):
            self.id = id
            self.timestamp = Twitter.globalTime
            Twitter.globalTime += 1
            self.next = None

        def get_id(self) -> int:
            return self.id

        def get_timestamp(self) -> int:
            return self.timestamp

        def get_next(self):
            return self.next

        def set_next(self,next_tweet):
            self.next = next_tweet

    class User:
        def __init__(self,id:int):
            self.id = id
            self.tweet_head = None
            self.followed_user_set = set()

        def get_id(self):
            return self.id

        def get_tweet_head(self) -> Tweet:
            return self.tweet_head

        def get_followed_user_set(self):
            return self.followed_user_set

        def __eq__(self, other):
            return self.id == other.id

        def follow(self, other):
            self.followed_user_set.add(other)

        def unfollow(self,other):
            self.followed_user_set.discard(other)

        def post(self, tweet:Tweet):
            # new tweet as the head of the linkedlist
            tweet.set_next(self.tweet_head)
            self.tweet_head = tweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        # if user does not exist create new user
        if userId not in self.idToUser:
            self.idToUser[userId] = Twitter.User(userId)
        user = self.idToUser[userId]
        user.post(Twitter.Tweet(tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if userId not in self.idToUser:
            return res
        # get follow list
        user = self.idToUser[userId]
        followed_user_set = user.get_followed_user_set()

        pq = []
        if user.get_tweet_head():
            heappush(pq,(-user.tweet_head.timestamp, user.get_tweet_head()))
        for other in followed_user_set:
            if other.get_tweet_head():
                heappush(pq,(-other.get_tweet_head().timestamp, other.get_tweet_head()))
        count = 0
        while pq and count < 10:
            _, tweet = heappop(pq)
            res.append(tweet.get_id())
            if tweet.get_next():
                heappush(pq,(-tweet.get_next().timestamp, tweet.get_next()))
            count += 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.idToUser:
            self.idToUser[followerId] = Twitter.User(followerId)
        if followeeId not in self.idToUser:
            self.idToUser[followeeId] = Twitter.User(followeeId)

        follower = self.idToUser[followerId]
        followee = self.idToUser[followeeId]

        follower.follow(followee)

    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.idToUser or followeeId not in self.idToUser:
            return  
        follower = self.idToUser[followerId]
        followee = self.idToUser[followeeId]

        follower.unfollow(followee)
            

        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)