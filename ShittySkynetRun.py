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


def rap_god(filename: str) -> List[List[str]]:
  """Makes rhymes"""
  f = open(filename, "r")
  big_list = []
  count = 0
  
  while count < 3:
    small_list = []
    empty = False
    while not empty:
      line = f.readline()
      if line != "\n" and line != "":
        small_list.append(line)
      else:
        empty = True
    
    big_list.append(small_list)
    count += 1
  
  return big_list


def strip_n_lines(lst: List[List[str]]) -> List[List[str]]:
  """Gets rid of \n"""
  for smol_list in lst:
    for c in range(len(smol_list)):
      word = smol_list[c]
      smol_list[c] = word.rstrip()
  return lst


def strip_recursive(lst: Union[List[Union[List, str]], str]) -> Union[List[Union[List, str]], str]:
  """Gets rid of \n recursively"""
  if isinstance(lst, str):
    return lst.rstrip()
  else:
    new_lst = []
    for item in lst:
      new_lst.append(strip_recursive(item))
    return new_lst


def talky_boi(lst: List[List[str]]) -> str:
  """Creates random message from the lists"""
  wordy_boi = ""
  for wordy_list in lst:
    index = random.randint(0, len(wordy_list) - 1)
    word = wordy_list[index]
    wordy_boi += word + " "
  return wordy_boi


if __name__ == '__main__':
  Amanda = Bot("uoft")
  Nancy = SingForMe(SHORT_LIST)
  plz_reply(Amanda, Nancy)
