import praw

class Bot:
  """Makes a beep boop"""
  subreddits = None
  comments = None
  
  def __init__(self, subs: str):
    # Change this part if you want to add your own account
    bot = praw.Reddit(user_agent = 'KindaFeeding',    
                      client_id = 'p_Y2_d0xk1Cm-Q',
                      client_secret = '8q469EsTHNUyRxg2LSUYRVlLiOc',
                      username = 'ShittySkynetBot',
                      password = 'Sh177y'
                      )
  
    self.subreddits = bot.subreddit(subs)
    self.comments = self.subreddits.stream.comments()
