# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:37:08 2015

@author: breiche

Women's Cup on Hackerrank

The Cabalistic Hills were created by Lucifer millions of years ago. 
They have N hills numbered 1 to N. The magical lamp is situated at the peak 
of hill N. Some of these hills are connected by one way rope bridges(directed),
 and these rope bridges are the only way to reach hill N and return back to 
 hill 1. Each rope bridge disappears after being used once.

Lucifer has created traps for the climbers. Some rope bridges do not lead to 
hill N, and some lead to hill N but without a way to return back to hill 1. 
Antony MUST use all the rope bridges in his journey from hill 1 to N and back 
to 1 or he is imprisoned by Lucifer.If multiple ropes are connecting two hills
then it should be counted multiple times and all of the ropes must be used 
once. You must advise Antony whether the hills are safe to climb or they are 
devious trap! Given N hills and M pairs of connected hills, determine whether 
it's a trap.
"""

import unittest

class HillsSolution(object):

    def Hills(self, n, bridges):
        '''
        This problem is a variant of the Seven Bridges problem! What we want is 
        to find out whether there is a Euler path in Lucifer's Hills.
        
        In the Koingesburg problem, the number of vertices of odd degree 
        may be either 0 or 2-- and if there are two vertices with odd degree, 
        then they are the starting and ending vertices.
        
        In this case, Antony must return to Hill #1, so there may be no
        odd vertices.
        
        N: an int, number of hills
        bridges: a list of pairs of hills, eg [1,4] = bridge between 1 and 4
        '''   
        try:
            
            unidircetional_ropes = {}
            bidirectional_bridges = {}
            for bridge in bridges:
                hill1, hill2 = int(bridge[0]), int(bridge[1])
                
                unidircetional_ropes.setdefault(hill1, []).append(hill2)
                
                bidirectional_bridges.setdefault(hill1, []).append(hill2)
                bidirectional_bridges.setdefault(hill2, []).append(hill1)
                            
            # in order to have a Eulerian path, all vertices must be even valence
            for hill, neighbors in bidirectional_bridges.items():
                if len(neighbors) % 2 == 1:
                    return "Danger!! Lucifer will trap you"
                    
            # we don't care about lone hills
            # unless they're the start or end hill, then we have a problem
            if 1 not in unidircetional_ropes or int(n) not in unidircetional_ropes:
                return "Danger!! Lucifer will trap you"
            
            # pruned graph must be connected, since Antony has to use all the bridges
            unvisited_hills = unidircetional_ropes.keys()
            hills_to_visit = Stack()
            hills_to_visit.push(1)
                    
            while True:
                if unvisited_hills == []:
                    return "Go on get the Magical Lamp"
                if hills_to_visit == []:
                    return "Danger!! Lucifer will trap you"
                
                current_hill = hills_to_visit.pop() 
                unvisited_hills.remove(current_hill)
    
                for neighbor in unidircetional_ropes[current_hill]:
                    if neighbor in unvisited_hills:
                        hills_to_visit.push(neighbor)
        except:
            return "Danger!! Lucifer will trap you"
                    
            
class Stack(list):
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self
    
class HillsTest(unittest.TestCase):
    
    def test1(self):
        s = HillsSolution()
        answer = s.Hills('4',[['1','2'], ['2','3'],['3','4'],['4','1']])
        expected = "Go on get the Magical Lamp"
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = HillsSolution()
        answer = s.Hills('4',[['1','2'], ['2','3'],['3','1']])
        expected = "Danger!! Lucifer will trap you"
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = HillsSolution()
        answer = s.Hills('5',[['1','2'], ['2','3'],['3','1'], ['4','5'], ['5','4']])
        expected = "Danger!! Lucifer will trap you"
        self.assertEqual(answer, expected)
        
    def test4(self):
        s = HillsSolution()
        answer = s.Hills('5',[['1','2'], ['2','5'],['5','1']])
        expected = "Go on get the Magical Lamp"
        self.assertEqual(answer, expected)
        
    def test5(self):
        s = HillsSolution()
        answer = s.Hills('5',[['1','2'], ['2','5'],['5','1'],['1', '3'], ['3', '1']])
        expected = "Go on get the Magical Lamp"
        self.assertEqual(answer, expected)
    

if __name__ == '__main__':
    unittest.main()

