# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:26:46 2015

@author: breiche

Find the median of two sorted arrays.
"""
import unittest

class MedianSortedArraySolution(object):

    def optimized_findMedianSortedArrays(self, nums1, nums2):
        '''
        Optimized solution
        If there are N elements in first array and M in the second array,
        runtime is O(log(N + M))
        
        Uses binary search like algorithm to find the Nth smallest element
        between two arrays.
        '''
        l = len(nums1) + len(nums2)
        if l % 2:
            return self.findNthSmallest(nums1, nums2, l/2 + 1)
        else:
            return (self.findNthSmallest(nums1, nums2, l/2) +
                    self.findNthSmallest(nums1, nums2, l/2 + 1))*0.5

    def findNthSmallest(self, nums1, nums2, n):
        if len(nums1) > len(nums2):
            return self.findNthSmallest(nums2, nums1, n)
        if not nums1:
            return nums2[n-1]
        if n == 1:
            return min(nums1[0], nums2[0])

        pa = min(n/2, len(nums1))
        pb = n-pa

        if nums1[pa-1] <= nums2[pb-1]:
            return self.findNthSmallest(nums1[pa:], nums2, n-pa)
        else:
            return self.findNthSmallest(nums1, nums2[pb:], n-pb)
           
    
    def naive_findMedianSortedArrays(self, nums1, nums2):
        """
        Naive solution:
        Combine both lists into a sorted list, then find the median of the 
        sorted list.
        
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
        
    def median(self, x):
        '''
        Returns median of a sorted list in O(1) time.
        '''
        if len(x) == 0:
            return 0
        elif len(x) % 2:
            return x[len(x)/2]
        else:
            midavg = (x[len(x)/2] + x[len(x)/2-1])/2.0
            return midavg   


class MedianArrayTest(unittest.TestCase):
    
    def naive_test1(self):
        s = MedianSortedArraySolution()
        answer = s.naive_findMedianSortedArrays([1,3,7,34], [6,10,14,15,16,17])
        expected = 12
        self.assertEqual(answer, expected)
    
    def naive_test2(self):
        s = MedianSortedArraySolution()
        answer = s.naive_findMedianSortedArrays([1,2,3,5,6,7], [4])
        expected = 4
        self.assertEqual(answer, expected)
        
    def naive_test3(self):
        s = MedianSortedArraySolution()
        answer = s.naive_findMedianSortedArrays([1], [2,3])
        expected = 2
        self.assertEqual(answer, expected)
        
    def naive_test_null_case(self):
        s = MedianSortedArraySolution()
        answer = s.naive_findMedianSortedArrays([], [])
        expected = 0
        self.assertEqual(answer, expected)
     
    def optimized_test1(self):
        s = MedianSortedArraySolution()
        answer = s.optimized_findMedianSortedArrays([1,3,7,34], [6,10,14,15,16,17])
        expected = 12
        self.assertEqual(answer, expected)
    
    def optimized_test2(self):
        s = MedianSortedArraySolution()
        answer = s.optimized_findMedianSortedArrays([1,2,3,5,6,7], [4])
        expected = 4
        self.assertEqual(answer, expected)
        
    def optimized_test3(self):
        s = MedianSortedArraySolution()
        answer = s.optimized_findMedianSortedArrays([1], [2,3])
        expected = 2
        self.assertEqual(answer, expected)
        
    def optimized_test_null_case(self):
        s = MedianSortedArraySolution()
        answer = s.optimized_findMedianSortedArrays([], [])
        expected = 0
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()
