"""Makes bots, docstrings are still dumb"""

import praw

class Bot: 
  bot = praw.Reddit(user_agent='KindaFeedingBot',
                    client_id='p_Y2_d0xk1Cm-Q',
                    client_secret='8q469EsTHNUyRxg2LSUYRVlLiOc',
                    username='ShittySkynetBot',
                    password='J19900101t'
                    )

  subreddit = bot.subreddit('uoft')
  multireddit = bot.subreddit('dankmemes+memeeconomy+meirl+me_irl+deepfriedmemes+classic4chan+bikinibottomtwitter+bertstrips+anime_irl+4chan+2meirl4meirl+prequelmemes')


  comments = subreddit.stream.comments()
  multicomments = multireddit.stream.comments()