# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:16:07 2015

@author: breiche

HackerRank Pythonist Challenge
Triangle Quest

You are given a positive integer N . 
You have to print a numerical triangle of height N−1  as shown below: 
1
22
333
4444
55555
......


Can you do it using only arithmetic operations, 
a single for loop and print statement? 
Note: Using anything related to strings will give a score of 0. 

"""
import unittest
import sys
from StringIO import StringIO

class TriangleQuestSolution(object):

        
    def printTriangle(self, k):
        '''
        prints a triangle, specified above, with height k.
        Does not use strings, uses a single for loop and print statment.
        '''
        for i in range(1, k):
            print i * self.buildIntFromList([1] * i)
   
    def buildIntFromList(self, nums):
        '''
        Builds a single integer, given a list of integers.
        By calculating which 'place' (eg., ones, tens, hundreds)
        the digit belongs in, and multiplying the number by 10 ^ (place - 1).
        '''
        return sum([digit * 10 ** (len(nums) - 1 - n) for n, digit in enumerate(nums)])
       
class SortDataTest(unittest.TestCase):
        
    def setUp(self):
        self.s = TriangleQuestSolution() 
        
    def test_triangle(self): 
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture

        self.s.printTriangle(5)
        expected = "1\n\
22\n\
333\n\
4444\n"
        sys.stdout = save_stdout
        answer = capture.getvalue()
        self.assertEqual(answer, expected) 

if __name__ == '__main__':
    unittest.main()
