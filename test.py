'''
per ricaricare lo script usa
import importlib
importlib.reload(module)

or

from importlib import reload
reload(module)

https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
'''

import numpy as np
from random import randint

def fun():
   print("hello world from the function")
   

def sigmoid(x):
   '''
   the function return the sigmoid of the given argument
   x = single value or array
   y = single value or array
   '''
   y = 1 / (1 + np.exp(-x) )
   return y
   
   
def prediction(w, x):
   '''
   w = weight vector (1 x d)
   x = feature vector (1 x d)
   y = output value, product of the two vectors above (scalar)
   '''
   
   #x = np.array([[1], x])
   
   print("w dim:", w.shape)
   print("x dim:", x.shape)
   
   y = np.dot(w, x.T)
   return y
   
   
   
def error(Y_hat, Y):
   '''
   Y_hat: predicted value (1 x M array)
   Y: real value (1 x M array)
   error : computed error (1 x M array)
   '''
   
   print("y_hat dim:", Y_hat.shape)
   print("y_hat dim:", Y.shape)
   
   if(Y_hat.shape != Y.shape):
      return -1
   
   error = np.dot( (Y_hat - Y), (Y_hat - Y).T )
   return error
   
   
def normalize(x):
   '''
   x = vector to normalize (1 x m)
   y = normalized vector (1 x m)
   '''
   
   tot = np.sum(x)
   y = x / tot
   return y
   
   
def computePower(x, exp):
   '''
   x = value to be considered (scalar)
   exp = exponential to be considered
   y = returned value (1 x exp)
   with 
   y = [x, x^2, x^3, ..., x^exp]
   '''
   y = np.zeros((1, exp))
   
   print(y.shape)
   
   for i in range(1, exp+1):
      y[0, i-1] = x ** i
      
   return y
   
   
   
def computeVectorPower(x, exp):
   '''
   x = value to be considered (1 x m)
   exp = exponential to be considered
   y = returned value (1 x (m x exp) )
   with 
   y = [x[0], x[0]^2, x[0]^3, ..., x[0]^exp, x[1], x[1]^2, x[1]^3, ..., x[1]^exp, ..., x[m]^exp]
   '''   
   
   print(x.shape)
   a, b = x.shape
   
   y = computePower(x[0, 0], exp)
   
   for i in range(1, b):
      #y = [y, computePower(x[0, i], exp)]
      local = computePower(x[0, i], exp)
      y = np.append(y, local)
   
   return y
   
   
def addOne(x):
   '''
   add "1" as first entry of the vector
   x = inpute vector (1 x m)
   y = output vector (1 x (m+1) )
   '''
   
   y = x
   y = np.append(1, y)
   return y
   
def writingTest():
   
   end = False
   lastWord = ""
   
   correct = 0
   wrong = 0
   
   dictionary = ["siege","niederlage","grenzen","wahnsinn", "guck mal","hohenflieger",
                          "enttauscht","entdecken","streiten","gewicht","gewalt","himmel","ho:lle",
                          "zwar","zufall","bleastigung","nun","zuverla:ssig","krigen"]	
   
   while(end == False):
     i = randint(0, len(dictionary)-1) 
     while(lastWord == dictionary[i]):
         i = randint(0, len(dictionary)-1) 
         
     correct_string=dictionary[i]
     #print(correct_string + ": ")
     local = input(correct_string + ": ")
      
     if(local != correct_string and local != 'q'):
        print("ERROR")
        wrong = wrong + 1
     elif (local == correct_string):
        correct = correct + 1
      
     if local == 'q':
        print("correct = ", correct)
        print("wrong = ", wrong)
        end = True
         
     lastWord = correct_string
      
      
def isFull(x):
   for i in range(1,len(x)):
      if(x[i] == 0):
         return False
         
   return True
      
      
def printString(word, found):
   '''
   word = string to be printed
   found = array used to print the string (1 = letter has been found, 0 = no)
   '''
   print(word[0], end="", flush=True)
         
   for i in range(1, len(word)):
      if(found[i] == 1):
         print(" " + word[i], end="", flush=True)
      else:
         print(" _", end="", flush=True)
         
   print();
         
      
def hangedMan():
   
   word = "test"
   found = [0]
   guessed = ""
   end = False
   
   for i in range(1, len(word)):
      found.append(0)
      #print(len(found))
   
   printString(word, found)
   
   while (end == False):
      
      guessed = input()
      
      #check if guessed word is presend in the word
      for i in range(1, len(word)):
         if (word[i] == guessed):
            found[i] = 1
       
      printString(word, found)
      
      end = isFull(found)
       
   print("gg ez")
      
   
def isCharOrNumber(x):
   if(x >= 'a' and x <= 'z'):
      return True
   if(x >= 'A' and x <= 'Z'):
      return True
   if(x >= '0' and x <= '9'):
      return True
   
   
   
def wordCounter():
   '''
   conta le parola nella stringa passata
   '''
   
   inword = False
   wordNumber = 0
   string = input()
   
   for i in range(0, len(string)):
      if(isCharOrNumber(string[i]) and inword == False):
         inword = True
         wordNumber = wordNumber + 1
      
      if(string[i] == ' '):
         inword = False
         
   print("total w c is : " + str(wordNumber))

   
   
wordCounter()   
#hangedMan() 
#writingTest()
#x = np.array([[1,2,3]])
#print(addOne(x))
#print(computeVectorPower(x, 4))
#a = np.loadtxt("file.txt")
