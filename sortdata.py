# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:43:37 2015

@author: bridgette

Hackerrank Pythonist Challenge: Sort Data

You are given data in a tabular format i.e. the data contains N  rows
 and each row contains M  space-separated elements. 

You can imagine the M  items to be different attributes (like height, 
weight, energy, etc) and each of the N  rows as an instance or a sample. 

Your task is to sort the table on the Kth  attribute and print the final 
resulting table. 

[If two attributes are the same for different rows, print the row that 
appeared first in the input]

"""
import unittest
import string 
import sys
from StringIO import StringIO

class SortDataSolution(object):

        
    def sortTable(self, table, k):
        '''
        sorts a table (given by a list-of-lists)
        by column k
        '''        
        self.k = k
        return sorted(table, key=self.getKthColumn)
    
    def getKthColumn(self, r):
        return r[self.k]
        
    def prettyPrintTable(self, table):
        for row in table:
            print string.join(map(str, row))
   

class SortDataTest(unittest.TestCase):
        
    def setUp(self):
        self.s = SortDataSolution()

    def test_sort(self):     
        answer = self.s.sortTable([[10, 2, 5], \
                                   [7, 1, 0],  \
                                   [9, 9, 9],  \
                                   [1, 23, 12],\
                                   [6, 5, 9]], 1)
                                   
        expected = [[7, 1, 0], \
                    [10, 2, 5],\
                    [6, 5, 9], \
                    [9, 9, 9], \
                    [1, 23, 12]]
                    
        self.assertEqual(answer, expected)  
        
    def test_prettyprint(self): 
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture

        table = self.s.sortTable([[10, 2, 5], \
                                   [7, 1, 0],  \
                                   [9, 9, 9],  \
                                   [1, 23, 12],\
                                   [6, 5, 9]], 1)
        self.s.prettyPrintTable(table)                      
        expected = "7 1 0\n\
10 2 5\n\
6 5 9\n\
9 9 9\n\
1 23 12\n"
        sys.stdout = save_stdout
        answer = capture.getvalue()
        self.assertEqual(answer, expected) 

if __name__ == '__main__':
    unittest.main()