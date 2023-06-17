"""Word Finder: finds random words from a dictionary."""
import fileinput
from random import randrange

class WordFinder:
   
    def __init__(self,file):
        self.files = file
        self.wordsread()
       
        
    
    def wordsread(self):
       '''opens the file, gets the lenth of the file, and displays length'''
       file = open(self.files, "r")
       lines = file.readlines()
       lens = len(lines)
       print(f'{lens} words read')
       file.close()
       
        
    def random(self):
      '''generates a random word based on how many words are availabe, and removes the last two letters'''
      self.file = open(self.files, "r")
      lines = self.file.readlines()
      lens = len(lines)
      num = randrange(lens)
      self.file.close()
      returnString = lines[num]
      strnLen = len(returnString)
      returnsString= returnString[0:strnLen -1]
      return returnsString
      
        

