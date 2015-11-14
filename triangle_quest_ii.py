# -*- coding: utf-8 -*-
'''
Created on Sat Nov 14 14:03:19 2015

@author: breiche
HackerRank Pythonist 3 Challenge

Triangle Quest II

You are given a positive integer N. 
Your task is to print a palindromic triangle of size N. 

For example, a palindromic triangle of size 5  is: 

1
121
12321
1234321
123454321


You can't take more than two lines. 
You have to complete the code using exactly one print statement. 

Note: 
Using anything related to strings will give a score of 0 . 
Using more than one for-statement will give a score of 0 .
'''

import unittest
import sys
from StringIO import StringIO

class TriangleQuestIISolution(object):

    def calculateTriangle(self, N):
        '''
        prints a triangle of size N.
        
        The sequence above is created by squaring repunits, and is 
        commonly called the Demlo numbers.
        
        A base 10 repunit can be calculated by:
        10^n - 1  / 9
        
        For more information, see:
        https://en.wikipedia.org/wiki/Repunit
        '''
        for e in range(1,int(N)+1):
            print ((10 **e -1 ) / 9 ) **2
   

class TriangleQuestIITest(unittest.TestCase):
        
    def setUp(self):
        self.s = TriangleQuestIISolution()

    def test_triangle(self): 
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture

        self.s.calculateTriangle(5)
        expected = "1\n\
121\n\
12321\n\
1234321\n\
123454321\n"
        sys.stdout = save_stdout
        answer = capture.getvalue()
        self.assertEqual(answer, expected)  

if __name__ == '__main__':
    unittest.main()