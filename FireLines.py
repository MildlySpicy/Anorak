"""Makes fire lines, still think docstrings are idiotic"""

from typing import List
from Lines import Line
import random

FULL_LIST = "SickRhymes.txt"
SHORT_LIST = "ShortRhymes.txt"
SUBREDDITS = "Subreddits.txt"


class SingForMe(Line):
  """Sings, fuck these docstrings"""

  def __init__(self, filename: str):
    Line.__init__(self, filename)
  
  def rap_for_me(self) -> str:
    """raps, how do i disable these docstrings on pycharm"""
    return self.talky_boi(self.lst)

  def talky_boi(self, lst: List[List[str]]) -> str:
    """Creates random message from the lists"""
    wordy_boi = ""
    for wordy_list in lst:
      index = random.randint(0, len(wordy_list) - 1)
      word = wordy_list[index]
      wordy_boi += word + " "
    return wordy_boi
  

class GiveMeMySubreddits(Line):
  """Gives subs"""

  def __init__(self, filename: str):
    Line.__init__(self, filename)

  def subreddits(self) -> List:
    """returns a subreddit list"""
    return self.lst

  def in_a_word(self) -> str:
    """Gives it in a word"""
    word = ""
    for sub in self.lst:
      word += "+" + sub
    return word


if __name__ == '__main__':
  bob = GiveMeMySubreddits(SUBREDDITS)
  print(bob.subreddits())
  print()
