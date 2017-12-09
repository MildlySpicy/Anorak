"""Docstrings are dumb"""

import praw
import random
import math
from typing import Optional, Tuple, List, Union

FULL_LIST = "SickRhymes.txt"
SHORT_LIST = "ShortRhymes.txt"


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
  

def dumbstuff(comment: str) -> str:
  """Creates the comment message"""
  message = ''
  lol = "\n\n Hi I am a bot. I don't work that well yet, ignore me please :)"

  if 'me too thanks' in comment.lower():
    message = 'meme too dank' + lol
  if 'metoothanks' in comment.lower():
    message = 'memetoodank' + lol

  return message


if __name__ == '__main__':
  a = rap_god(SHORT_LIST)
  print(a)
  print("")
  print("")
  b = strip_n_lines(a)
  print(b)
  print("")
  print("")
  c = strip_recursive(a)
  print(c)
  print("")
  print("")
  
  for _ in range(6):
    print(talky_boi(c))
    print("----")
  
  # for retarded_reply in multicomments:                  # Change this line for multi
  #   send = dumbstuff(str(retarded_reply.body))
  #   if send != '':
  #     retarded_reply.reply(send)
