# https://leetcode.com/problems/design-twitter/

from collections import defaultdict, deque


class Twitter:

  def __init__(self):
    self.following = defaultdict(set)
    self.tweets = defaultdict(deque)
    self.time = 0

  def postTweet(self, userId: int, tweetId: int) -> None:
    self.tweets[userId].appendleft((self.time, tweetId))
    self.time += 1

  def getNewsFeed(self, userId: int) -> List[int]:
    combined_tweets = deque()
    combined_tweets.extend(self.tweets[userId])
    for followeeId in self.following[userId]:
      combined_tweets.extend(self.tweets[followeeId])

    combined_tweets = sorted(combined_tweets, reverse=True)

    recent_tweetIds = []
    for timestamp, tweetId in combined_tweets[:10]:
      recent_tweetIds.append(tweetId)

    return recent_tweetIds

  def follow(self, followerId: int, followeeId: int) -> None:
    self.following[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    if followeeId in self.following[followerId]:
      self.following[followerId].remove(followeeId)


