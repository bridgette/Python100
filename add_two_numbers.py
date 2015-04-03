# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:35:20 2015

@author: bridgette
"""
import unittest

class ListNode:
     ''' Definition for singly-linked list.''' 
     def __init__(self, x, next_node = None):
         self.val = x
         self.next = next_node


class Two_Numbers_Solution:
    '''
    https://leetcode.com/problems/add-two-numbers/
    You are given two linked lists representing two non-negative numbers. 
    The digits are stored in reverse order and each of their nodes contain 
    a single digit. 
    Add the two numbers and return it as a linked list.
    
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    '''
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        
        first_node = node = ListNode(0)
        while l1 != None or l2 != None or carry:
            v1 = v2 = 0             
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            new_val = v1 + v2 + carry
            if new_val > 9:
                carry = 1
                new_val = new_val % 10
            else:
                carry = 0
                
            node.next = ListNode(new_val)
            node = node.next
            
        return first_node.next
                
    
class two_numbers_test(unittest.TestCase):
    def test_example(self):
        s = Two_Numbers_Solution()
        # 243
        n1 = ListNode(2, ListNode(4, ListNode(3, None)))
        # 564
        n2 = ListNode(5, ListNode(6, ListNode(4, None)))
        answer = s.addTwoNumbers(n1, n2)
        expected = ListNode(7, ListNode(0, ListNode(8, None)))
        while True:
            if answer == None or expected == None: 
                break;
            self.assertEqual(answer.val, expected.val)
            answer = answer.next
            expected = expected.next
        
        self.assertEqual(expected, None)
        self.assertEqual(answer, None)
        
    def test_5_5(self):
        # 5 + 5 = 10
        s = Two_Numbers_Solution()
        n1 = ListNode(5, None)
        n2 = ListNode(5, None)
        answer = s.addTwoNumbers(n1, n2)
        expected = ListNode(0, ListNode(1, None))
        while True:
            if answer == None or expected == None: 
                break;
            self.assertEqual(answer.val, expected.val)
            answer = answer.next
            expected = expected.next
            
        self.assertEqual(expected, None)
        self.assertEqual(answer, None)
    
    def test_0_0(self):
        s = Two_Numbers_Solution()
        n1 = ListNode(0, None)
        n2 = ListNode(0, None)
        answer = s.addTwoNumbers(n1, n2)
        expected = ListNode(0, None)
        while True:
            if answer == None or expected == None: 
                break;
            self.assertEqual(answer.val, expected.val)
            answer = answer.next
            expected = expected.next
            
        self.assertEqual(expected, None)
        self.assertEqual(answer, None)
        
if __name__ == '__main__':
    unittest.main()

    
