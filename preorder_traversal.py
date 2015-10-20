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

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def preOrderTree(self):
        '''
        Uses tail recursion to get the preordered list of the binary tree.
        '''
        if(self.root != None):
            return self._preOrderTree(self.root, [])

    def _preOrderTree(self, node, preordered_list):
        if(node == None):
            return preordered_list
        preordered_list.append(node.v)
        preordered_list = self._preOrderTree(node.l, preordered_list)
        preordered_list = self._preOrderTree(node.r, preordered_list)
        return preordered_list

      
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
        if len(l) > len(set(l)): return "no"
        
        tree = Tree()
        for each_l in l:
            tree.add(each_l)
        preordered_list = tree.preOrderTree()
        if preordered_list == l:
            return "yes"
        else:
            return "no"
   

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