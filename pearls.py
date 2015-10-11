# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:37:08 2015

@author: breiche

Women's Cup on Hackerrank

The state of California is facing a serious drought. Antony wants to save the 
state by winning the heart of Tialoc, the supreme rain god. Tialoc gives Antony
 a task to complete first. He gives Antony N pearls. These pearls are magical.
 When Antony restrings two pearls together, the two pearls combine to make a 
 single pearl. Each pearl has an associated cost. When the two pearls become 
 one, the cost of each individual pearl is added together to become the cost 
 of the combined pearl. So if cost of first pearl is c 1   and cost of second 
 pearl if c 2   then cost of combined pearl will be (c 1 +c 2 ) modulo (10 9 +7) .

Antony has to restring N pearls together in such a way that the cost of the 
final pearl is the absolute minimum. Antony can only restring two pearls at a 
time. Succeeding in this task will cause Tialoc to shower California with rain!
 Help Antony restring the pearls! 

"""

import unittest
import heapq
import numpy

class PearlsSolution(object):
    def Pearls(self, n, pearl_cost):
        '''
        n: number of  on the string
        pearl_cost: list of ints representing cost of joining pearls
    
        It always makes sense to merge the two smallest pearls on the string
        '''   
        running_cost = 0
        heapq.heapify(pearl_cost)
        
        while n > 1:
            i = heapq.heappop(pearl_cost)
            j = heapq.heappop(pearl_cost)
            running_cost = running_cost + i + j     
            heapq.heappush(pearl_cost, i + j)
            n = n - 1
            
        return running_cost % (10 ** 9 + 7)
        
    def Pearls_numpy(self, n, pearl_cost):
        '''
        n: number of  on the string
        pearl_cost: list of ints representing cost of joining pearls
    
        It always makes sense to merge the two smallest pearls on the string
        '''   
        running_cost = 0
        pearl_cost = numpy.array(pearl_cost, numpy.float)
        
        while n > 1:
            i = numpy.argmin(pearl_cost)
            cost_pearl_one = pearl_cost[i]
            pearl_cost[i] = numpy.inf
            
            j = numpy.argmin(pearl_cost)
            cost_pearl_two = pearl_cost[j]
            
            combined_cost = (cost_pearl_one + cost_pearl_two) % (10 ** 9 + 7)
            pearl_cost[j] = combined_cost

            running_cost = running_cost + combined_cost    

            n = n - 1
            
        return running_cost % (10 ** 9 + 7)
        
class PearlsTest(unittest.TestCase):
    
    def test1(self):
        s = PearlsSolution()
        answer = s.Pearls(7, [2,4,1,2,10,2,3])
        expected = 59 % (10 ** 9 + 7)
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = PearlsSolution()
        answer = s.Pearls(5, [6,5,4,1,2])
        expected = 39 % (10 ** 9 + 7)
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = PearlsSolution()
        answer = s.Pearls_numpy(7, [2,4,1,2,10,2,3])
        expected = 59 % (10 ** 9 + 7)
        self.assertEqual(answer, expected)
        
    def test4(self):
        s = PearlsSolution()
        answer = s.Pearls_numpy(5, [6,5,4,1,2])
        expected = 39 % (10 ** 9 + 7)
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()

