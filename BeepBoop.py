"""Makes bots, docstrings are still dumb"""

import praw


class Bot:
  """Its a bot, wow"""

  subreddits = None
  comments = None
  
  def __init__(self, subs: str):
    bot = praw.Reddit(user_agent = 'KindaFeeding',    # add your own deets
                      client_id = '',
                      client_secret = '',
                      username = '',
                      password = ''
                      )
  
    self.subreddits = bot.subreddit(subs)
    self.comments = self.subreddits.stream.comments()
