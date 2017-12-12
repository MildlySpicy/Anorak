"""Docstrings are dumb"""

import random
from typing import List, Union
from BeepBoop import Bot
from FireLines import SingForMe

FULL_LIST = "SickRhymes.txt"
SHORT_LIST = "ShortRhymes.txt"


def plz_reply(bullet_bill: Bot, killer_koopa: SingForMe):
  """Replys to the comments"""
  for comment in bullet_bill.comments:
    send = dumbstuff(str(comment.body), killer_koopa)
    if send != '':
      comment.reply(send)
      

def dumbstuff(comment: str, koopa: SingForMe) -> str:
  """Creates the comment message"""
  message = ''
  lol = "\n\n Hi I am a bot. I don't work that well yet, ignore me please :)"

  if 'me too thanks' in comment.lower():
    message = koopa.rap_for_me() + lol
  if 'metoothanks' in comment.lower():
    message = koopa.rap_for_me().rstrip(" ") + lol
  
  return message


if __name__ == '__main__':
  Amanda = Bot("uoft")
  Nancy = SingForMe(SHORT_LIST)
  plz_reply(Amanda, Nancy)
