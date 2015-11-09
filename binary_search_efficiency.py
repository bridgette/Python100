# -*- coding: utf-8 -*-
"""
Binary Search Efficiency Doubter
author: bridgette
10/19/2015

The binary search is a classic algorithm in computer science. For this problem 
we will use the following pseudocode to define our binary search:
Perform a binary search on the array a with values in a[0] through a[n-1] to 
find, if it exists, the value x. The values in the array a may be assumed to 
be in strictly increasing order.

    Low = 0
    High = n – 1
    While Low <= High
        Mid = (Low + High) / 2 [We assume integer division truncates.]
        If a[Mid] = x then return FOUND
        If a[Mid] < x then Low = Mid + 1
        If a[Mid] > x then High = Mid – 1
    If we fall out of the while loop, return NOT_FOUND


Professors teach that this is an efficient algorithm with a worst case number 
of times through the loop of roughly log base 2 of n and an average case that 
is slightly better than that. A student who is not convinced decides to build 
lists of various sizes and search for every number in the list and keep track 
of how many times the loop is executed. In the following example, the number of 
times the loop is executed to find each value is indicated below the 
corresponding value.

It should be clear that any list of length 7 will have a total loop count of 17
under the assumptions that the list is sorted and all the values are different. 
That is, the length of the list determines the total loop count.

The problem here is to determine the total loop count given the length of the 
list. You may assume that the answer for any test case in the input fits in a 
signed 64-bit integer.

"""
import unittest

class BinarySearchEfficiencySolution():
    
    def BinarySearch(self, seq, x):
        '''
        Returns the number of iterations that binary search takes to find x in 
        list seq.
        '''
        num_iterations = 0
        min = 0
        max = len(seq) - 1
        while True:
            num_iterations += 1
            if max < min:
                return -1
            m = (min + max) // 2
            if seq[m] < x:
                min = m + 1
            elif seq[m] > x:
                max = m - 1
            else:
                return num_iterations


    def CalcTotalLoops_Naive(self, n):
        '''
        Calculates the number of loops needed to binary search every element
        in a list in O(n log(n)) time.
        
        Creates a unique, sorted list length n, and calls BinarySearch on 
        each element. BinarySearch returns the number of iterations required
        to find element in the list.
        '''
        total_loops = 0
        unique_sorted_list = [i for i in range(n)]
        for i in range(n):
            loops_for_i = self.BinarySearch(unique_sorted_list, i)
            total_loops = total_loops + loops_for_i
        return total_loops
        
    def CalcTotalLoops_Optimized(self, n):
        '''
        Calculates the number of loops needed to binary search every element in
        a list in O(log (n)) time.
        
        In a 'perfect' case, the length of the list can be written as:
        2 ^ 0 + 2 ^ 1 + 2 ^ 2 + ...+ 2 ^ i
        The middle is always found, and the sublists are also balanced. 
        e.g.,
        n = 7
        n = 2^0 + 2^1 + 2^2
        Thus indicating that a list of size n = 7 has one middle element
        (2^0=1), two subtrees on its left and right (2^1=2), and four 
        sub-subtrees (2^2=4).

        If the length of the list cannot be written as the above summation,
        then we must take into account the 'remainder.'         
        where remainder = n - (2^0 +...+2^i).
        
        The remainder means that we might need additional searching in one of
        the branches, because we might've rounded down when calculating the
        middle.
        '''
        total_loops = 0
        curr_loops = 1
        i = 0
        
        while True:
            if n - 2 ** i < 0: # remainder!
                total_loops = total_loops + n * curr_loops
                break
            else:
                n = n - 2**i
                total_loops = total_loops + (2**i * curr_loops)
                curr_loops = curr_loops + 1
                i = i + 1
            
        return total_loops
    

class BinarySearchEfficiencyTester(unittest.TestCase):
        
    def setUp(self):
        self.s = BinarySearchEfficiencySolution()

    def test_naive(self):     
        answer = self.s.CalcTotalLoops_Naive(3)
        expected = 5
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Naive(4)
        expected = 8
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Naive(7)
        expected = 17
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Naive(8)
        expected = 21
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Naive(9)
        expected = 25
        self.assertEqual(answer, expected) 
              
        answer = self.s.CalcTotalLoops_Naive(124)
        expected = 748
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Naive(321)
        expected = 2387
        self.assertEqual(answer, expected) 
        
    def test_optimized(self):         
        
        answer = self.s.CalcTotalLoops_Optimized(3)
        expected = 5
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Optimized(4)
        expected = 8
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Optimized(7)
        expected = 17
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Optimized(8)
        expected = 21
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Optimized(9)
        expected = 25
        self.assertEqual(answer, expected) 
        
        
        answer = self.s.CalcTotalLoops_Optimized(124)
        expected = 748
        self.assertEqual(answer, expected) 
        
        answer = self.s.CalcTotalLoops_Optimized(321)
        expected = 2387
        self.assertEqual(answer, expected) 
        
        


if __name__ == '__main__':
    unittest.main()

''' # to run from stdin
s = BinarySearchEfficiencySolution()
case = 0
while True:
    try:
        numbers_on_line = raw_input().split()
        for n in numbers_on_line:
            case = case + 1
            print "Case", str(case) + ":", s.CalcTotalLoops_Naive(int(n))
    except EOFError as e:
        break
'''