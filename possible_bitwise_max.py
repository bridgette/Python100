# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:32:41 2015

@author: breiche

Women's Cup on Hackerrank
"""

import unittest

class PossibleMaxSolution(object):
    def PossibleMax(self, n, k):
        """
        You are given a set S = {1, 2, 3,…,N }. Find two integers A and B (A<B)  
        from the set S such that the value of A  & B  is the maximum possible 
        and less than the given integer K. In this case, & represents the 
        operator bitwise AND.
        """
        max_value = 0
        for b in range(n+1):
            for a in range(b): 
                bitwise_ab = a & b
                if bitwise_ab > max_value and bitwise_ab < k:
                    max_value = bitwise_ab
        return max_value
        
class PossibleMaxTest(unittest.TestCase):
    
    def test1(self):
        s = PossibleMaxSolution()
        answer = s.PossibleMax(5,2)
        expected = 1
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = PossibleMaxSolution()
        answer = s.PossibleMax(8,5)
        expected = 4
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = PossibleMaxSolution()
        answer = s.PossibleMax(2,2)
        expected = 0
        self.assertEqual(answer, expected)

        
if __name__ == '__main__':
    unittest.main()
