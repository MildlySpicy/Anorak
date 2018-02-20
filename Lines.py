import random
from typing import List, Union

FULL_LIST = "SickRhymes.txt"
SHORT_LIST = "ShortRhymes.txt"
SUBREDDITS = "Subreddits.txt"

class Line:
  """Parent class for all classes that need to create lists from text files"""

  lst: List
  name: str
  
  def __init__(self, filename: str) -> None:
    self.name = filename
    self.lst = self.read_file()
        
  def read_file(self) -> List[List[str]]:
    """Reads"""
    f = open(self.name, "r")
    big_list = []
    count = 0
    max = get_n(self.name)
    
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

    clean = simpler(strip_recursive(big_list))
    
    return clean

def get_n(filename: str) -> int:
  """returns number of \n only lines in the file"""
  counter = 0
  g = open(filename, "r")
  line = "a"
  while line != '':
    line = g.readline()
    if line == '\n':
      counter += 1
  return counter
  
def strip_recursive(lst: Union[List[Union[List, str]], str]) -> Union[List[Union[List, str]], str]:
  """Gets rid of \n recursively"""
  if isinstance(lst, str):
    return lst.rstrip()
  else:
    new_lst = []
    for item in lst:
      clean = strip_recursive(item)
      if clean != []:
        new_lst.append(clean)
    return new_lst

def simpler(lst: List[List[str]]) -> Union[List[str], List[List[str]]]:
  """Removes redundant lists and empty lists"""
  if len(lst) == 1:
    return lst[0]
  else:
    clean = []
    for smol_lst in lst:
      if smol_lst != []:
        clean.append(smol_lst)
    return clean

if __name__ == '__main__':
  mary = Line(SHORT_LIST)
  print(mary.lst)
