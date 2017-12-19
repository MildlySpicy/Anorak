"""Makes bots, docstrings are still dumb"""

import praw


class Bot:
  """Its a bot, wow"""

  subreddits = None
  comments = None
  
  def __init__(self, subs: str):
    bot = praw.Reddit(user_agent = 'KindaFeeding',
                      client_id = 'p_Y2_d0xk1Cm-Q',
                      client_secret = '8q469EsTHNUyRxg2LSUYRVlLiOc',
                      username = 'ShittySkynetBot',
                      password = 'J19900101t'
                      )
  
    self.subreddits = bot.subreddit(subs)
    self.comments = self.subreddits.stream.comments()
