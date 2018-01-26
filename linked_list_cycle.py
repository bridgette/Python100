"""
@author:bridgette
1/26/2018
"""

import unittest

 
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class CycleSolution:
    '''
    checks to see if there is a cycle in the linked list
    by storing/checking memory locations of nodes in a dictionary.
    Space Complexity: O(N), where N is length of linked list.
    Average time complexity O(1), worst case O(N)
    '''
    def __init__(self):
        self.seen_nodes = {}    
    
    def has_cycle(self, head):
        if not (head):
            return False
        
        curr = head

        while(True):
            if (id(curr) in self.seen_nodes.keys()):
                return True
            elif (curr.next):
                self.seen_nodes[id(curr)] = True
                curr = curr.next
            else:
              return False  

class TestCycleSolution(unittest.TestCase):

    def test_empty(self):
        s = CycleSolution()
        n = None
        answer = s.has_cycle(n)
        expected = False
        self.assertEqual(answer, expected)

    def test_no_cycle(self):
        s = CycleSolution()
        n1 = Node("a", Node("b", Node("c", None)))
        answer = s.has_cycle(n1)
        expected = False
        self.assertEqual(answer, expected)

    def test_has_cycle(self):
        s = CycleSolution()
        n1 = Node("a")
        n2 = Node("b")
        n1.next = n2
        n2.next = n1
        answer = s.has_cycle(n1)
        expected = True
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()
        
