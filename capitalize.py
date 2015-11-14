# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:24:28 2015

@author: breiche

HackerRank Pythonist 3 Challenge

You are given a string S. 
Your task is to capitalize each word of S.

Whitespace must be preserved.

"""
import unittest
import re 
class CapitalizeSolution(object):

        
    def capitalize(self, s):
        '''
        capitalizes every word in s while preserving whitespace.
        '''       
        return re.sub("(^|\s)(\S)", self.repl_func, s)
    
    def repl_func(self, m):
        '''
        process regular expression match groups for word upper-casing problem
        '''
        return m.group(1) + m.group(2).upper()
                   
class CapsTest(unittest.TestCase):
        
    def setUp(self):
        self.s = CapitalizeSolution() 
        
    def test(self): 
        answer = self.s.capitalize("hello world")
        expected = "Hello World"
        self.assertEqual(answer, expected) 
        
    def test_langston_hughes(self):
        answer = self.s.capitalize("Besides, They see how beautiful I am \
And be ashamed. I too sing America")
        expected = "Besides, They See How Beautiful I Am And Be Ashamed. I \
Too Sing America"
        self.assertEqual(answer, expected) 
        
    def test_null(self):
        answer = self.s.capitalize("")
        expected = ""
        self.assertEqual(answer, expected)
        
    def test_whitespace_preserved(self):
        answer = self.s.capitalize("ab 1a ab     a ")
        expected = "Ab 1a Ab     A "
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()

