# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:26:46 2015

@author: breiche

Finds the median of two sorted arrays.
"""
import unittest

class MedianSortedArraySolution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return
   
class MedianArrayTest(unittest.TestCase):
    
    def test1(self):
        s = MedianSortedArraySolution()
        answer = s.findMedianSortedArrays([1,3,7,34], [6,10,14,15,16,17])
        expected = 10
        self.assertEqual(answer, expected)
    
    def testArraysNotSorted(self):
        s = MedianSortedArraySolution()
        try:
            s.findMedianSortedArrays([1,4,2], [8,7,6])
        except:
            assert(True)

        
if __name__ == '__main__':
    unittest.main()
