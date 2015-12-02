# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:06:06 2015

@author: breiche

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N. 


"""

import unittest

class Multiples35Solution():
    
    def Multiples35_Naive(self, N):
        '''
        Returns the sum of all multiples of three and five < N.
        '''
        return sum(self.GenerateThreeFive(N))
    
    def GenerateThreeFive(self, N):
        ''' 
        generates all multiples of 3 and five below N.
        python generators are lazy evaluators (saves on space).
        '''
        n = 0
        while n < N:
            if n % 3 == 0 or n % 5 == 0:
                yield n
            n += 1
            
    def Multiples35_Optimized(self, N):
        '''
        Can simplify this to run in O(1) time using the formula to add an 
        arithmetic series.
        '''
       
        sum_threes = (3/2)*(3 + N)  
        sum_fives  = (5/2)*(5 + N)
        
        return sum_threes + sum_fives

class Multiples35Test(unittest.TestCase):
        
    def setUp(self):
        self.s = Multiples35Solution()

    def test(self):     
        answer = self.s.Multiples35_Naive(10)
        expected = 23
        self.assertEqual(answer, expected) 
        
        answer = self.s.Multiples35_Optimized(10)
        expected = 23
        self.assertEqual(answer, expected) 
               
        


if __name__ == '__main__':
    unittest.main()
