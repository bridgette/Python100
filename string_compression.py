# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:23:11 2015

@author: breiche

Hackerrank Pythonist 3 Challenge

String Compression

You are given a string S . Suppose a character 'c ' occurs consecutively X 
times in the string. Replace these consecutive occurrences of the character 
'c ' with (X,c)  in the string. 

Constraints
All the characters of S denote integers between 0 and 9. 

1 ≤∣S∣≤ 10^4  

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)


Explanation:

First, the character 1 occurs only once. It is replaced by (1,1). 
Then the character 2 occurs three times, and it is replaced by (3,2),
and so on. 

Also, note the single space within each compression 
and between the compressions. 

"""

import unittest
import sys

class CompressionSolution(object):

    def compress(self, s):
        '''
        implements a basic compression algorithm.
        worst case, (on an input like 121212...) 
        actually extends the input size by x2.
        
        returns an ordered list of tuples with (char, # occurences).
        '''
        if s == "": 
            return []
        
        compression = []
        
        #count the first character
        current_char = s[0]
        occurences = 1
        
        for c in s[1:]:
            if c == current_char:
                occurences += 1
            else:
                compression.append((occurences, current_char))
                current_char = c
                occurences = 1
        
        # count the last run
        compression.append((occurences, current_char))
        return compression
        
    def prettyPrint(self, l):
        '''
        pretty-prints the list of tuples for grading.
        '''
        for t in l:
            c, o = t
            sys.stdout.write( "(" + str(c) + ", " + str(o) + ") " )

        
class CompressionTest(unittest.TestCase):
        
    def setUp(self):
        self.s = CompressionSolution() 
        
    def test_compression(self): 
        answer = self.s.compress("1222311")
        expected = [(1, '1'), (3, '2'), (1, '3'), (2, '1')]
        self.assertEqual(answer, expected) 
        
    def test_null(self): 
        expected = []
        answer = self.s.compress("")
        self.assertEqual(answer, expected) 
        


if __name__ == '__main__':
    unittest.main()
