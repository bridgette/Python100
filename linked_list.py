# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:08:15 2015

@author: bridgette
"""
import unittest
import string

class Node(object):
    '''
    Represents a node in a singly-linked list
    ''' 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedListSolution(object):
    
    def PrintLinkedList(self, head):
        '''
        prints a singly-linked list, if given the head node
        '''   
        data = []
        while head and head.data:
            data.append(str(head.data))
            head = head.next
        return string.join(data, "\n")
        
    def ReversePrint(self, head):
        '''
        prints a singly-linked list in reverse order, if given the head node
        '''
        data = []
        while head and head.data:
            data.append(str(head.data))
            head = head.next
        data.reverse()
        return string.join(data, "\n")
        
    def InsertTail(self, head, data):
        '''
        Inserts data at the back of a linked list, then returns the head
        of the same linked list back.
        
        Runs in O(n), where n is length of linked list, because program must 
        traverse the entire linked list.
        '''
        i = head
        
        if not i or not i.data: # if linked list is empty or starts with empty node
            i = Node(data)
            return i
        
        while i.next:
            i = i.next

        i.next = Node(data)
        return head
        
    def InsertHead(self, head, data):
        '''
        Inserts data at the head of a linked list, and returns the new head of
        the linked list back.
        O(1) time to create a new node with data, and assign previous head node
        to newHead.next
        '''
        newHead = Node(data, head)
        return newHead
        
    def InsertNth(self, head, data, position):
        '''
        Insert a node at Nth position. Runs in O(position), where position
        is the input argument. Worst case runs in O(L), where L is the length 
        of the linked list.
        '''
        i = head

        if not i or not i.data or position == 0:
            return self.InsertHead(head, data)
                    
        p = 1
        while i.next and p < position:
            i = i.next            
            p += 1
                
        left_side = i
        right_side = i.next
        left_side.next = Node(data, right_side)
        
        return head
            
    def DeleteNth(self, head, position):
        ''' 
        Delete node from linked list at position, where head is the pointer
        to the first node in the linked list. 
        
        Runs in O(position), where position
        is the input argument. Worst case runs in O(L), where L is the length 
        of the linked list.
        '''        
        if position == 0: 
            return head.next
        if not head or not head.data:
            return None
        
        i = head
        p = 0
        prev_node = None
        while i.next and p < position:
            prev_node = i
            i = i.next            
            p += 1  
            
        next_node = i.next
        prev_node.next = next_node
        
        return head


        
class LinkedListTest(unittest.TestCase):
    
    def setUp(self):
        self.one_two_three = Node(1, Node(2, Node(3)))
        self.empty_list = None
        self.empty_node = Node()
        self.long_list = Node(1, Node(2, Node(6, Node(9, Node(4, Node(7))))))
        
    def test_print(self):
        s = LinkedListSolution()
        answer_123 = s.PrintLinkedList(self.one_two_three)
        expected_123 = "1\n2\n3"
        self.assertEqual(answer_123, expected_123)
        
        answer_empty = s.PrintLinkedList(self.empty_list)
        expected_empty = ""
        self.assertEqual(answer_empty, expected_empty)
        
        answer_123 = s.PrintLinkedList(self.long_list)
        expected_123 = "1\n2\n6\n9\n4\n7"
        self.assertEqual(answer_123, expected_123)
        
    def test_print_reverse(self):
        s = LinkedListSolution()
        answer_123 = s.ReversePrint(self.one_two_three)
        expected_123 = "3\n2\n1"
        self.assertEqual(answer_123, expected_123)
        
        answer_empty = s.ReversePrint(self.empty_list)
        expected_empty = ""
        self.assertEqual(answer_empty, expected_empty)
        
        answer_long = s.ReversePrint(self.long_list)
        expected_long = "7\n4\n9\n6\n2\n1"
        self.assertEqual(answer_long, expected_long)
        
    def test_insert_tail(self):
        s = LinkedListSolution()

        answer = s.InsertTail(self.one_two_three, 4)
        answer = s.PrintLinkedList(answer)
        expected = "1\n2\n3\n4"
        self.assertEqual(answer, expected)
        
        answer = s.InsertTail(self.empty_list, 1)
        answer = s.PrintLinkedList(answer)
        expected = "1"
        self.assertEqual(answer, expected)
        
        answer = s.InsertTail(self.empty_node, 1)
        answer = s.PrintLinkedList(answer)
        expected = "1"
        self.assertEqual(answer, expected)

        answer = s.InsertTail(self.long_list, 42)
        answer = s.PrintLinkedList(answer)
        expected = "1\n2\n6\n9\n4\n7\n42"
        self.assertEqual(answer, expected)
        
    def test_insert_head(self):
        s = LinkedListSolution()

        answer = s.InsertHead(self.empty_list, 1)
        answer = s.PrintLinkedList(answer)
        expected = "1"
        self.assertEqual(answer, expected)
        
        answer = s.InsertHead(self.one_two_three, 4)
        answer = s.PrintLinkedList(answer)
        expected = "4\n1\n2\n3"
        self.assertEqual(answer, expected)
        
        answer = s.InsertHead(self.empty_node, 1)
        answer = s.PrintLinkedList(answer)
        expected = "1"
        self.assertEqual(answer, expected)

        answer = s.InsertHead(self.long_list, 42)
        answer = s.PrintLinkedList(answer)
        expected = "42\n1\n2\n6\n9\n4\n7"
        self.assertEqual(answer, expected)
        
        
    def test_insert_nth(self):
        s = LinkedListSolution()

        answer = s.InsertNth(self.one_two_three, 4, 0)
        answer = s.PrintLinkedList(answer)
        expected = "4\n1\n2\n3"
        self.assertEqual(answer, expected)
        
        answer = s.InsertNth(self.one_two_three, 4, 3)
        answer = s.PrintLinkedList(answer)
        expected = "1\n2\n3\n4"
        self.assertEqual(answer, expected)
        
        answer = s.InsertNth(self.empty_list, 1, 0)
        answer = s.PrintLinkedList(answer)
        expected = "1"
        self.assertEqual(answer, expected)
        
        answer = s.InsertNth(self.empty_node, 1, 0)
        answer = s.PrintLinkedList(answer)
        expected = "1"
        self.assertEqual(answer, expected)

        answer = s.InsertNth(self.long_list, 42, 0)
        answer = s.PrintLinkedList(answer)
        expected = "42\n1\n2\n6\n9\n4\n7"
        self.assertEqual(answer, expected)
        
        answer = s.InsertNth(self.long_list, 42, 3)
        answer = s.PrintLinkedList(answer)
        expected = "1\n2\n6\n42\n9\n4\n7"
        self.assertEqual(answer, expected)
        
    def test_delete_nth(self):
        s = LinkedListSolution()

        answer = s.DeleteNth(self.one_two_three, 0)
        answer = s.PrintLinkedList(answer)
        expected = "2\n3"
        self.assertEqual(answer, expected)
        
        answer = s.DeleteNth(self.one_two_three, 2)
        answer = s.PrintLinkedList(answer)
        expected = "1\n2"
        self.assertEqual(answer, expected)
        
        answer = s.DeleteNth(self.empty_list, 1)
        answer = s.PrintLinkedList(answer)
        expected = ""
        self.assertEqual(answer, expected)
        
        answer = s.DeleteNth(self.empty_node, 1)
        answer = s.PrintLinkedList(answer)
        expected = ""
        self.assertEqual(answer, expected)

        answer = s.DeleteNth(self.long_list, 4)
        answer = s.PrintLinkedList(answer)
        expected = "1\n2\n6\n9\n7"
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()

