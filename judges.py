# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:19:35 2015

@author: bridgette

Your team has been retained by the director of a competition who supervises a 
panel of judges. The competition asks the judges to assign integer scores to 
competitors – the higher the score, the better. Although the event has 
standards for what score values mean, each judge is likely to interpret 
those standards differently. A score of 100, say, may mean different things 
to different judges.

The director's main objective is to determine which competitors should 
receive prizes for the top positions. Although absolute scores may differ 
from judge to judge, the director realizes that relative rankings provide 
the needed information – if two judges rank the same competitors first, 
second, third, ... then they agree on who should receive the prizes.

Your team is to write a program to assist the director by comparing the 
scores of pairs of judges. The program is to read two lists of integer 
scores in competitor order and determine the highest ranking place (first 
place being highest) at which the judges disagree.

"""


import unittest
      
class JudgesSolution():
          
    def Judge(self, n, j1, j2):
        '''
        Compares scores of two judges, j1 and j2. Determines highest ranking
        place at which the judges agree, and returns it (or "agree" if they 
        agree completely).
        '''
        j1_rank_map = {}
        j2_rank_map = {}
        for rank in range(n):
            continue

        return "agree"
   

class PreorderTraversalTester(unittest.TestCase):
        
    def setUp(self):
        self.s = JudgesSolution()

    def test_example(self):     
        answer = self.s.Judge(4, [3, 8, 6, 2], [15, 37, 17, 3])
        expected = "agree"
        self.assertEqual(answer, expected) 

    def test_example2(self):
        answer = self.s.Judge(8, [80, 60, 40, 20, 10, 30, 50, 70], \
        [160, 100, 120, 80, 20, 60, 90, 135])
        expected = 3
        self.assertEqual(answer, expected) 
        
    def test_null(self):
        answer = self.s.Judge([], [])
        expected = "agree"
        self.assertEqual(answer, expected)  


if __name__ == '__main__':
    unittest.main()

''' # to run from stdin
s = PreorderTraversalSolution()
case = 0
while True:
    try:
        tree = []
        numbers_on_line = raw_input().split()
        for n in numbers_on_line:
            if int(n) >= 0:
                tree.append(int(n))
            if int(n) < 0:
                case = case + 1
                print "Case", str(case) + ":", s.CheckPreorder(tree)
                tree = []
    except EOFError as e:
        break
'''

