# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:57:45 2015

@author: breiche

Alphabet Rangoli
You are given an integer, N . Your task is to print an 
alphabet rangoli of size N .

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------

The center of the rangoli has the first alphabet letter a, 
and the boundary has the Nth alphabet letter (in alphabetical order).
"""


import unittest
import sys
from StringIO import StringIO

class RangoliSolution(object):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def Rangoli(self, n):
        '''
        prints a rangoli of size n.
        
        builds from the middle; adds each new line above and below (since rangoli
        are symmetric).
        
        each row will have length:
        = 1 center letter 'a' + 2 * (n-1 letters) + 2 * (n-1 dashes)
        = 1 + 4 * (n-1)
        '''
        rangoli = ""
        rangoli_row_length = 1 + 4 * (n - 1)

        for r in range(n):
            letters_in_row = self.alphabet[r:n]
            row = self.calculateRangoliRow(letters_in_row, rangoli_row_length)
            
            if rangoli == "": # middle row doesn't repeat
                rangoli = row
            else:
                rangoli = row + '\n' + rangoli + '\n' + row
                
        print rangoli
            
    def calculateRangoliRow(self, letters_to_fill, row_length):
        '''
        given a sequential list of letters and a row length, returns the 
        formatted rangoli row.
        '''
        row = ['-'] * row_length
        middle = row_length / 2 # row_length will always be odd
        double = lambda x: x*2
        current_letter = 0
        
        for offset_from_middle in map(double, range(len(letters_to_fill))):
            letter_locations = set([middle + offset_from_middle,\
                                   middle - offset_from_middle])
            for index in letter_locations:
                row[index] = letters_to_fill[current_letter]
            current_letter += 1 
        return ''.join(row)
        

                   
class CapsTest(unittest.TestCase):
        
    def setUp(self):
        self.s = RangoliSolution() 
        
    def test_size_three(self): 
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        
        answer = self.s.Rangoli(3)
        expected ="----c----\n\
--c-b-c--\n\
c-b-a-b-c\n\
--c-b-c--\n\
----c----\n"

        sys.stdout = save_stdout
        answer = capture.getvalue()
        self.assertEqual(answer, expected) 
        
    def test_size_five(self): 
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        
        answer = self.s.Rangoli(5)
        expected ="--------e--------\n\
------e-d-e------\n\
----e-d-c-d-e----\n\
--e-d-c-b-c-d-e--\n\
e-d-c-b-a-b-c-d-e\n\
--e-d-c-b-c-d-e--\n\
----e-d-c-d-e----\n\
------e-d-e------\n\
--------e--------\n"
        sys.stdout = save_stdout
        answer = capture.getvalue()
        self.assertEqual(answer, expected) 
        
    def test_size_ten(self):
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        
        answer = self.s.Rangoli(10)
        expected ="------------------j------------------\n\
----------------j-i-j----------------\n\
--------------j-i-h-i-j--------------\n\
------------j-i-h-g-h-i-j------------\n\
----------j-i-h-g-f-g-h-i-j----------\n\
--------j-i-h-g-f-e-f-g-h-i-j--------\n\
------j-i-h-g-f-e-d-e-f-g-h-i-j------\n\
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----\n\
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--\n\
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j\n\
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--\n\
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----\n\
------j-i-h-g-f-e-d-e-f-g-h-i-j------\n\
--------j-i-h-g-f-e-f-g-h-i-j--------\n\
----------j-i-h-g-f-g-h-i-j----------\n\
------------j-i-h-g-h-i-j------------\n\
--------------j-i-h-i-j--------------\n\
----------------j-i-j----------------\n\
------------------j------------------\n"
        sys.stdout = save_stdout
        answer = capture.getvalue()
        self.assertEqual(answer, expected) 
        
if __name__ == '__main__':
    unittest.main()

