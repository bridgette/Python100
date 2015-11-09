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

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        
        if (val < node.v):                # insert on the left
            if (node.r != None):
                raise AssertionError("Out of preorder!")
            elif (node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
                
        elif (val > node.v):              # insert on the right
            if (node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)
                
        else:                             # val == node.v
            raise AssertionError("Cannot insert duplicate elements!")
      
class PreorderTraversalSolution():
          
    def CheckPreorder(self, l):
        '''
        Returns whether list l represents a valid preorder of a binary 
        search tree, by inserting all elements of l into a binary tree
        and comparing the preorder of the tree to the order of l.
        
        Building the binary search tree takes O(n^2), and traversing it takes
        O(n). Total runtime is then O(n^2).
        
        output: "yes" or "no"
        '''        
        tree = Tree()
        
        for each_l in l:
            try:
                tree.add(each_l)
            except AssertionError:
                return "no"

        return "yes"
   

class PreorderTraversalTester(unittest.TestCase):
        
    def setUp(self):
        self.s = PreorderTraversalSolution()

    def test_123(self):     
        answer = self.s.CheckPreorder([2,3,1])
        expected = "no"
        self.assertEqual(answer, expected) 
        
        answer = self.s.CheckPreorder([1, 2, 3])
        expected = "yes"
        self.assertEqual(answer, expected) 
        
        answer = self.s.CheckPreorder([1, 3, 2])
        expected = "yes"
        self.assertEqual(answer, expected) 
        
        answer = self.s.CheckPreorder([2, 1, 3])
        expected = "yes"
        self.assertEqual(answer, expected) 
        
        answer = self.s.CheckPreorder([3, 2, 1])
        expected = "yes"
        self.assertEqual(answer, expected) 
        
        answer = self.s.CheckPreorder([3, 1, 2])
        expected = "yes"
        self.assertEqual(answer, expected) 
        
    def test_dupes(self):
        answer = self.s.CheckPreorder([3, 3, 1, 2])
        expected = "no"
        self.assertEqual(answer, expected) 
        
    def test_medium(self):
        answer = self.s.CheckPreorder([50, 30, 20, 10, 25, 40, 45, 70, 90, 80])
        expected = "yes"
        self.assertEqual(answer, expected) 
        
    def test_null(self):
        answer = self.s.CheckPreorder([])
        expected = "yes"
        self.assertEqual(answer, expected)  
        
        answer = self.s.CheckPreorder([-1765432])
        expected = "yes"
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