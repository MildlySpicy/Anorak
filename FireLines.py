"""Makes fire lines, still think docstrings are idiotic"""

from typing import List
from Lines import Line


class SingForMe(Line):
  """Sings, fuck these docstrings"""
  
  def __init__(self, filename: str):
    Line.__init__(self, filename)
  
  def rap_for_me(self) -> str:
    """raps, how do i disable these docstrings on pycharm"""
    return Line.lst_rhymes
  

class GiveMeMySubreddits(Line):
  """Gives subs"""

  def __init__(self, filename: str):
    Line.__init__(self, filename)

  def subreddits(self) -> str:
    """returns a subreddit list"""
    return Line.lst
