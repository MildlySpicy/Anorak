"""Docstrings are dumb"""

from BeepBoop import Bot
from FireLines import SingForMe, GiveMeMySubreddits
from time import gmtime, strftime
# import prawcore
# import praw

FULL_LIST = "SickRhymes.txt"
SHORT_LIST = "ShortRhymes.txt"
SUBREDDITS = "Subreddits.txt"
ALL_SUBS = "Allofthem.txt"


def plz_reply(bullet_bill: Bot, killer_koopa: SingForMe):
  """Replys to the comments"""
  for comment in bullet_bill.comments:
    send = dumbstuff(str(comment.body), killer_koopa)
    if send != '':
      print("[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "] sent a dumb comment")
      comment.reply(send)

def dumbstuff(comment: str, koopa: SingForMe) -> str:
  """Creates the comment message"""
  message = ''
  lol = "\n\n *^(Hi I am a bot. I make rhymes.)* \n\n *^(I don't work that well yet, ignore me please ;3)*"

  if 'me too thanks' in comment.lower():
    message = koopa.rap_for_me() + lol
  if 'metoothanks' in comment.lower():
    message = koopa.rap_for_me().rstrip(" ") + lol
  
  return message


if __name__ == '__main__':
  print("initializing skynet...")
  Kavan = GiveMeMySubreddits(SUBREDDITS)
  subs = Kavan.in_a_word()
  print("")
  print("Subreddits used: ")
  for sub in Kavan.subreddits():
    print("/r/" + sub)

  print("")
  print("skynet v1.3.37 has been initialized")
  print("prepare for world dominashun:")

  Amanda = Bot(subs)
  Nancy = SingForMe(SHORT_LIST)
  plz_reply(Amanda, Nancy)