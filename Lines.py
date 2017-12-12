"""Parent class for all classes that need to create lists from text files"""

import random
from typing import List, Union

FULL_LIST = "SickRhymes.txt"
SHORT_LIST = "ShortRhymes.txt"


class Line:
  """Makes a crapton of lines"""
  
  lst_rhymes: List
  lst: List
  
  def __init__(self, filename: str):
    self.lst = self.read_file(filename)
    self.lst_rhymes = self.strip_recursive(self.lst)
    
  def read_file(self, filename: str) -> List[List[str]]:
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
        new_lst.append(self.strip_recursive(item))
      return new_lst

  def talky_boi(self, lst: List[List[str]]) -> str:
    """Creates random message from the lists"""
    wordy_boi = ""
    for wordy_list in lst:
      index = random.randint(0, len(wordy_list) - 1)
      word = wordy_list[index]
      wordy_boi += word + " "
    return wordy_boi


if __name__ == '__main__':
  pass
  
  # a = read_file(SHORT_LIST)
  # b = strip_n_lines(a)
  # c = strip_recursive(a)
  #
  # for _ in range(6):
  #   print(talky_boi(c))
  #   print("----")
