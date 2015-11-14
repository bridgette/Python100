# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:33:59 2015

@author: breiche

HackerRank Pythonist 3 Challenge
Triangle Quest

ginortS

You are given a string S . 
S  contains alphanumeric characters only. 
Your task is to sort the string S  in the following manner:
•All sorted lowercase letters are ahead of uppercase letters. 
•All sorted uppercase letters are ahead of digits.
•All sorted odd digits are ahead of sorted even digits.

a) Using join, for or while anywhere in your code, even as substrings, 
will result in a score of 0. 

b) You can only use one  sorted function in your code. 
 A 0 score will be awarded for using sorted more than once. 
"""
import unittest
from array import array

class ginortSolution(object):

    def sort(self, s):
        s_prime = sorted(s, key=self.constraints)
        return array('B', map(ord, s_prime)).tostring()
        
    def constraints(self, char):
        score = 0
        score = score + ord(char)
        if char.islower(): 
            score = score -200
        elif char.isupper(): 
            score = score - 100
        elif str.isdigit(char) and int(char) % 2 == 0: # even
            score = score + 10
        return score

        
class ginortSTest(unittest.TestCase):
        
    def setUp(self):
        self.s = ginortSolution() 
        
    def test(self): 
        expected = "ginortS1324"
        answer = self.s.sort("Sorting1234")
        self.assertEqual(answer, expected) 
        
    def test_null(self): 
        expected = ""
        answer = self.s.sort("")
        self.assertEqual(answer, expected) 
        
    def test_alpha(self): 
        expected = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        answer = self.s.sort("yzrGaxHAqFEDmICpBJwesKoltLnMvbXNuWkdVOUhPjTQRZYSgicf")
        self.assertEqual(answer, expected) 
        


if __name__ == '__main__':
    unittest.main()

