# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 08:36:01 2015

@author: bridgette
"""
import unittest

class Longest_Substring_Solution:
    '''
    Given a string, find the length 
    of the longest substring without repeating characters.    
    '''
    def lengthOfLongestSubstring_naive(self, s):
        '''
        Consider all substrings and check each for unique characters.
        Where N is length of string, there will be 
        ( N choose 1) + .... (N choose N) possible strings
        each of which can be evaluated in O(N) time, for a total of O(N^3).
        '''
    
    def lengthOfLongestSubstring(self, s):
        '''
        Solves longest non-repeating substring problem in linear time.
        Scan the string left to right, keep a map of visited characters => 
        their index for the current substring.
        '''
        visited = {}
        max_length = 0 
        curr_length = 0
        
        for index, char in enumerate(s):
            
            if char in visited.keys() and visited[char] >= index - curr_length:
                
                max_length = max(max_length, curr_length)

                # new substring starts after last instance of repeated char
                curr_length = index - visited[char]
                              
                
            else:
                curr_length = curr_length + 1   

                max_length = max(max_length, curr_length)
            
            visited[char] = index
                
        return max_length
                

class Longest_Substring_Test(unittest.TestCase):
    
    def test1(self):
        s = Longest_Substring_Solution()
        answer = s.lengthOfLongestSubstring("abcabcbb")
        expected = 3
        self.assertEqual(answer, expected)

    def test2(self):
        s = Longest_Substring_Solution()
        answer = s.lengthOfLongestSubstring("bbbb")
        expected = 1
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = Longest_Substring_Solution()
        answer = s.lengthOfLongestSubstring("tmmzuxt")
        expected = 5
        self.assertEqual(answer, expected)
        
    def test4(self):
        s = Longest_Substring_Solution()
        answer = s.lengthOfLongestSubstring("abccab")
        expected = 3
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()
