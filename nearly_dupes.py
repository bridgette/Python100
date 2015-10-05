# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:19:19 2015

@author: breiche

Given an array of integers, find out whether there are two distinct indices i 
and j in the array such that the difference between nums[i] and nums[j] is at 
most t and the difference between i and j is at most k. 
"""

import unittest

class NearlyDupeSolution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        return True
        
class AlmostDupeTest(unittest.TestCase):
    
    def test1(self):
        s = NearlyDupeSolution()
        answer = s.containsNearbyAlmostDuplicate([1,2,17,46,3,4], 1, 10)
        expected = True
        self.assertEqual(answer, expected)

        
if __name__ == '__main__':
    unittest.main()
