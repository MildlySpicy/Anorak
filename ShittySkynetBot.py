"""FUCK YOUR DOCSTRING BITCH"""

import praw

bot = praw.Reddit(user_agent='KindaFeedingBot',
                  client_id=,                   # add your own details
                  client_secret=,
                  username=, 
                  password=
                  )

subreddit = bot.subreddit('guttar')
multireddit = bot.subreddit('dankmemes+memeeconomy+meirl+me_irl+deepfriedmemes+classic4chan+bikinibottomtwitter+bertstrips+anime_irl+4chan+2meirl4meirl+prequelmemes')


comments = subreddit.stream.comments()
multicomments = multireddit.stream.comments()

def dumbstuff(comment: str) -> str:
  message = ''
  lol = "\n\n Hi I am a bot. I don't work that well yet, ignore me please :)"

  if 'me too thanks' in comment.lower():
    message = 'meme too dank' + lol
  if 'metoothanks' in comment.lower():
    message = 'memetoodank' + lol

  return message


for retarded_reply in multicomments:                  # Change this line for multi
  send = dumbstuff(str(retarded_reply.body))
  if send != '':
    retarded_reply.reply(send)
