"""Parent class for all classes that need to create lists from text files"""

import random
from typing import List, Union

FULL_LIST = "SickRhymes.txt"
SHORT_LIST = "ShortRhymes.txt"
SUBREDDITS = "Subreddits.txt"


class Line:
  """Makes a crapton of lines"""

  lst: List
  
  def __init__(self, filename: str) -> None:
    self.lst = self.strip_recursive(self.read_file(filename))
    
  def read_file(self, filename: str) -> List[List[str]]:
    """Reads"""
    f = open(filename, "r")
    big_list = []
    count = 0
    max = self.get_n(filename)
    
    while count < max + 1:
      small_list = []
      empty = False
      while not empty:
        line = f.readline()
        if line != "\n" and line != "":
          small_list.append(line)
        else:
          empty = True
      
      if small_list != []:
        big_list.append(small_list)
      count += 1
    
    return big_list

  def get_n(self, filename: str) -> int:
    """returns number of \n only lines in the file"""
    counter = 0
    g = open(filename, "r")
    line = "a"
    while line != '':
      line = g.readline()
      if line == '\n':
        counter += 1
    return counter

  def strip_n_lines(self, lst: List[List[str]]) -> List[List[str]]:
    """Gets rid of \n"""
    for smol_list in lst:
      for c in range(len(smol_list)):
        word = smol_list[c]
        smol_list[c] = word.rstrip()
    return lst
  
  def strip_recursive(self, lst: Union[List[Union[List, str]], str]) -> Union[List[Union[List, str]], str]:
    """Gets rid of \n recursively"""
    if isinstance(lst, str):
      return lst.rstrip()
    else:
      new_lst = []
      for item in lst:
        clean = self.strip_recursive(item)
        if clean != []:
          new_lst.append(clean)
      return new_lst


if __name__ == '__main__':
  bob = Line(SHORT_LIST)
  # print(bob.lst)
  print(bob.get_n(SHORT_LIST))
  print(bob.get_n(SUBREDDITS))
  
  a = bob.read_file(SHORT_LIST)
  # d = bob.read_file_better(SHORT_LIST)
  c = bob.strip_recursive(a)
  # e = bob.strip_recursive(a)
  # b = strip_n_lines(a)
  
  
  # print(a)
  # print(d)
  print(c)
  # print(e)
  # for _ in range(6):
  #   print(talky_boi(c))
  #   print("----")
