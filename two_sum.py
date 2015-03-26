# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:22:00 2015

@author: bridgette
"""
import unittest

class Solution:
    '''
    https://leetcode.com/problems/two-sum/
    Given an array of integers, find two numbers 
    such that they add up to a specific target number.
    Returns indices of two numbers such that they add to target,
    where index1 < index2. Indices are *not* zero based.
    Assume each input has one solution.
    '''
        
    def naive_two_sum(self, num, target):
        '''
        Nested loops that iterate over length of 'num' means this solution
        runs O(n^2) time.
        '''
        for index_1 in range(0, len(num)):
            for index_2 in range(len(num[:index_1]) + 1, len(num)):
                if num[index_1] + num[index_2] == target:
                    return (index_1 + 1, index_2 + 1)
    
    def optimized_two_sum(self, num, target):
        '''
        Uses a dictionary to speed up the runtime by storing the 
        numbers we've seen before with their indicies.
        Python dictionary __contains__ method ("key in d.keys()") 
        runs in O(1), so this solution is O(n).
        '''
        d = {}
        for index, num in enumerate(num, 1):
            if target-num in d.keys():
                return d[target-num], index
            else:            
                d[num] = index
            
                    
class Test_Two_Sum(unittest.TestCase):

    def test_naive_two_sum(self):
        s = Solution()
        self.assertEqual( s.naive_two_sum([2, 1, 3], 4),  (2,3) )
        self.assertEqual( s.naive_two_sum([1,2,3,4,5,6,7], 13),  (6,7) )
        self.assertEqual( s.naive_two_sum([1,1], 2),  (1,2) )
        self.assertEqual( s.naive_two_sum([95, 0], 95),  (1,2) )
        
    def test_optimized_two_sum(self):
        s = Solution()
        self.assertEqual( s.optimized_two_sum([2, 1, 3], 4),  (2,3) )
        self.assertEqual( s.optimized_two_sum([1,2,3,4,5,6,7], 13),  (6,7) )
        self.assertEqual( s.optimized_two_sum([1,1], 2),  (1,2) )
        self.assertEqual( s.optimized_two_sum([95, 0], 95),  (1,2) )
        
        
if __name__ == '__main__':
    unittest.main()
        