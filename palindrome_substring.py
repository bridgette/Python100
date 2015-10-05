# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:26:29 2015

@author: breiche
"""
import unittest

class PalindromeSubstringSolution(object):
    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        
        Given a string S, find the longest palindromic substring in S. You may 
        assume that the maximum length of S is 1000, and there exists one 
        unique longest palindromic substring.
        '''
        
        
class PalindromeTest(unittest.TestCase):
    
    def test_racecar(self):
        s = PalindromeSubstringSolution()
        answer = s.longestPalindrome("I want to buy a racecar bed at Ikea.")
        expected = "racecar"
        self.assertEqual(answer, expected)
        
    def test_bananas(self):
        s = PalindromeSubstringSolution()
        answer = s.longestPalindrome("bananas")
        expected = "anana"
        self.assertEqual(answer, expected)
        
    def test_panama(self):
        s = PalindromeSubstringSolution()
        answer = s.longestPalindrome("amanaplanacanalpanama")
        expected = "amanaplanacanalpanama"
        self.assertEqual(answer, expected)
    
    def test_null(self):
        s = PalindromeSubstringSolution()
        answer = s.longestPalindrome("")
        expected = ""
        self.assertEqual(answer, expected)

        
if __name__ == '__main__':
    unittest.main()

        