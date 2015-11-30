# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:19:18 2015

@author: breiche

Project Euler
Prime Factorization

The prime factors of 13195 are 5, 7, 13 and 29. 

What is the largest prime factor of a given number N?
"""

import unittest
from math import ceil

class PrimeFactorSolution(object):
    
    def SieveOfErathosthenes(self, n):
        '''
        Generates all primes up to n using the Sieve of Erathosthenes. 
        Starting with all multiples of 2, it iteratively marks all non-prime 
        numbers up to n, leaving only the primes.
        '''
        candidates = [1] * (n + 1)
        
        # 0 and 1 are not primes
        if n > -1:
            candidates[0] = 0
        if n > 0:
            candidates[1] = 0 
        
        i = 0 
        while (i < n):
            # advance to the next prime
            while (i < n and candidates[i] == 0):
                i += 1
            if i < n:
                # cross out multiples of the prime, starting with 2 * j
                for j in range(2, int(ceil(n/i))):
                    candidates[j*i] = 0
                i += 1
        
        all_primes = [c for c, flag in enumerate(candidates) if flag == 1]
        return all_primes
        
    def FindLargestFactor(self, n):
        '''
        First calculates all possible primes using the Sieve of 
        Erathosthenes.
        Then, checks to see whether the primes are a factor of n.
        '''        
        primes = self.SieveOfErathosthenes(n-1)
        primes.reverse()
        for p in primes:
            if n % p == 0:
                return p
        return n
    
class PrimeTest(unittest.TestCase):
    def setUp(self):
        self.s = PrimeFactorSolution()
 
    def test_negatives(self):
       answer = self.s.FindLargestFactor(-13)
       expected = -13
       self.assertEqual(answer, expected) 
       
       answer = self.s.FindLargestFactor(-8)
       expected = -8
       self.assertEqual(answer, expected)
        
    def test_one(self):
        answer = self.s.FindLargestFactor(1)
        expected = 1
        self.assertEqual(answer, expected) 
        
    def test_primes(self):
        answer = self.s.FindLargestFactor(2)
        expected = 2
        self.assertEqual(answer, expected) 
        
        answer = self.s.FindLargestFactor(13)
        expected = 13
        self.assertEqual(answer, expected) 
        
    def test_nonprimes(self):
        answer = self.s.FindLargestFactor(8)
        expected = 2
        self.assertEqual(answer, expected) 
        
        answer = self.s.FindLargestFactor(35)
        expected = 7
        self.assertEqual(answer, expected) 
        
    def test_large(self):
        answer = self.s.FindLargestFactor(13195)
        expected = 29
        self.assertEqual(answer, expected) 
        
if __name__ == '__main__':
    unittest.main()
    
