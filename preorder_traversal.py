# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:53:02 2015

@author: breiche

A preorder traversal is defined by the following recursive pseudocode:
preorder_traversal(root)
    print the value in root [in general, process the value, but we will just 
    print it]
    if root has a left subtree
        preorder_traversal(left subtree of root)
    if root has a right subtree
        preorder_traversal(right subtree of root)


A preorder traversal of the above binary search tree would give 
50, 30, 20, 10, 25, 40, 45, 70, 90, 80.

Note that 2, 3, 1 is not the preorder traversal of any binary search tree 
since 2 would have to be in the root as the first value printed and then 
either 3 would be on the left side or 1 would be on the right side since 1 
comes after 3 in the preorder traversal.

The problem here is to read a list of numbers and determine if it is the 
preorder traversal of a binary search tree.

"""

import unittest

class PreorderTraversalSolution():
    
    def CheckPreorder(self, l):
        '''
        Returns whether list l represents a valid preorder of a binary 
        search tree.
        
        output: "yes" or "no"
        '''
        return "yes"


   

class PreorderTraversalTester(unittest.TestCase):
        
    def setUp(self):
        self.s = PreorderTraversalSolution()


    def test(self):     
        answer = self.s.CheckPreorder([2,3,1])
        expected = "no"
        self.assertEqual(answer, expected) 
        
        answer = self.s.CheckPreorder([50, 30, 20, 10, 25, 40, 45, 70, 90, 80])
        expected = "yes"
        self.assertEqual(answer, expected) 
        


if __name__ == '__main__':
    unittest.main()

''' # to run from stdin
s = PreorderTraversalSolution()
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