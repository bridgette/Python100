# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:42:26 2015

@author: breiche

Women's Cup on Hackerrank
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:32:41 2015

@author: breiche


Project Earth, California's biggest environmental organization, is working to 
protect the planet Earth from global warming. Dr. Ritika is a scientist at 
Project Earth. She created a chemical called K29 which can increase the 
absorption rate of carbon dioxide by plants and help reduce global warming.

Unfortunately, K29 is not reacting the way it should. Dr. Ritika noticed that 
when K29 is used in plants, the reaction time is exactly T seconds. However, 
the chemical's reaction time changes as time passes, by following a specific 
pattern. It will change by 1 second every two hours, alternately increasing or 
decreasing every two hours. For the first two hours, the reaction time 
DECREASES by 1  second. During the next two hours, the reaction time INCREASES 
by 2  seconds. Then, for the next two hours, the reaction time DECREASES by 3  
seconds. The reaction time follows this pattern by incremental seconds until 
the Nth hour.

Dr. Ritika needs the final reaction time in the Nth hour to correct K29. As her
 assistant, you must help Dr. Ritika correct the error so that she can save 
 planet Earth. 
 Given the value of N and an initial reaction time, T, find the final reaction 
 time after N hours.
 
Constraints 
1 ≤ N ≤ 10^16 
1 ≤ T ≤ 10^16

"""

import unittest
import math

class ProjectEarthSolution(object):
    def naive_ProjectEarth(self, n, t):
        '''
        Computes the current reaction time by 
        stepping through every hour.
        '''
        curr_hours = 0
        curr_T = t
        reaction_delta = -1
        
        while curr_hours < n:
            curr_hours = curr_hours + 1

            if curr_hours % 2 == 1 and curr_hours > 1:
                if reaction_delta <= 0:
                    reaction_delta = abs(reaction_delta) + 1
                elif reaction_delta > 0:
                    reaction_delta = -1 * (abs(reaction_delta) + 1)
                    
            curr_T = curr_T + reaction_delta     

        return curr_T
        
    def optimized_ProjectEarth(self, n, t):
        '''
        n = num hours
        t = initial reaction time
        Runs in O(1), since the reaction can be broken down into 4-hour cycles.
        
        During the first hour, reaction changes by 
            -(cycle# * 2 - 1)
        During the first and second hours, reaction changes by 
            -2(cycle# * 2 - 1)
        During the first-third hours, reaction changes by 
            -2(cycle# * 2 - 1) + (cycle# * 2)
        
        Therefore, the delta(t) of an entire cycle is always +2.
        '''
        # total change from all full 4-hour cycles
        num_cycles = math.floor(n / 4)
        delta = num_cycles * 2
        
        # where are we in the last, partial 4-hour cycle?
        last_cycle = num_cycles + 1
        if n % 4 == 1:
            delta = delta - (last_cycle * 2 - 1)
        elif n % 4 == 2:
            delta = delta -2 * (last_cycle * 2 - 1)
        elif n % 4 == 3:
            delta = delta -2 * (last_cycle * 2 - 1) + (last_cycle * 2)
            
        return t + delta
        
class ProjectEarthTest(unittest.TestCase):
    
    def test1(self):
        s = ProjectEarthSolution()
        answer = s.optimized_ProjectEarth(5,3)
        expected = 2
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = ProjectEarthSolution()
        answer = s.optimized_ProjectEarth(2,5)
        expected = 3
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = ProjectEarthSolution()
        answer = s.optimized_ProjectEarth(4,0)
        expected = 2
        self.assertEqual(answer, expected)
        
    def test4(self):
        s = ProjectEarthSolution()
        answer = s.optimized_ProjectEarth(0,12)
        expected = 12
        self.assertEqual(answer, expected)

        
if __name__ == '__main__':
    unittest.main()

