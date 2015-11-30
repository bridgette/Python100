# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:28:46 2015
@author: bridgette

Project Euler 
Largest Palindromic Product 

A palindromic number reads the same both ways. The smallest 6 digit 
palindrome made from the product of two 3-digit numbers is 

101101=143×707

Find the largest palindrome made from the product of two 3-digit numbers 
which is less than N . 
"""

import unittest

class PalindromicProductSolution(object):
        
    def FindLargestPalindrome(self, n):
        '''
        Finds a number that meets following requirements:
        1. less than n 
        2. a palindrome (same forwards and backwards)
        3. product of two 3-digit numbers
        '''
        return 111111
    
class PrimeTest(unittest.TestCase):
    def setUp(self):
        self.s = PalindromicProductSolution()
 
    def test_one(self):
        answer = self.s.FindLargestPalindrome(101110)
        expected = 101101
        self.assertEqual(answer, expected) 
        
    def test_over_8000(self):
        answer = self.s.FindLargestPalindrome(800000)
        expected = 793397
        self.assertEqual(answer, expected) 

        
if __name__ == '__main__':
    unittest.main()
    


