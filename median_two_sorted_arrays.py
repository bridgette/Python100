# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:26:46 2015

@author: breiche

Find the median of two sorted arrays.
"""
import unittest

class MedianSortedArraySolution(object):
    def median(self, x):
        '''
        Returns median of a sorted list in O(1) time.
        '''
        if len(x) == 0:
            return 0
        elif len(x) % 2 != 0:
            return x[len(x)/2]
        else:
            midavg = (x[len(x)/2] + x[len(x)/2-1])/2.0
            return midavg   
            
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Naive solution:
        If there are N elements in the first array and M in the second array, 
        runtime is O(N + M).
        """
        in_order = []
        index_1 = 0
        index_2 = 0

        while index_1 < len(nums1) or index_2 < len(nums2):
            
            if index_1 < len(nums1):
                num1 = nums1[index_1]
            else:
                num1 = float('inf')
            
            if index_2 < len(nums2):
                num2 = nums2[index_2]
            else:
                num2 = float('inf')
            
            if num1 < num2:
                in_order.append(num1)
                index_1 = index_1 + 1 
            else:
                in_order.append(num2)
                index_2 = index_2 + 1 
                            
        return self.median(in_order)


class MedianArrayTest(unittest.TestCase):
    
    def test1(self):
        s = MedianSortedArraySolution()
        answer = s.findMedianSortedArrays([1,3,7,34], [6,10,14,15,16,17])
        expected = 12
        self.assertEqual(answer, expected)
    
    def test2(self):
        s = MedianSortedArraySolution()
        answer = s.findMedianSortedArrays([1,2,3,5,6,7], [4])
        expected = 4
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = MedianSortedArraySolution()
        answer = s.findMedianSortedArrays([1], [2,3])
        expected = 2
        self.assertEqual(answer, expected)
        
    def test_null_case(self):
        s = MedianSortedArraySolution()
        answer = s.findMedianSortedArrays([], [])
        expected = 0
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()
