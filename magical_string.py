# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:57:10 2015

@author: breiche
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:42:26 2015

@author: breiche

Women's Cup on Hackerrank
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:32:41 2015

@author: breiche

Julia is trying to generate a magical string S consisting of only '1' and '2'. 
The string is magical because concatenating the number of contiguous 
occurrences of characters '1' and '2' generates the string S itself.

As the string contains an infinite amount of characters, it is not possible 
for Julia to generate the whole string. She managed to generate the first few 
characters only:
•S = 122112122122112112…… 

Concatenating the number of contiguous occurrences produces 12211212212……  
and this is the string S itself.

Julia knows that you can generate the magical string S, so she wants you to 
answer two types of queries:
•1 N : Count the number of occurrences of '1' between positions 1 and N inclusively.
•2 N : Count the number of occurrences of '2' between positions 1 and N inclusively.


T = 1 or 2 
1 ≤ N ≤ 5×10^6  


Women's Cup on Hackerrank

"""

import unittest

class MagicalStringSolution(object):
    def MagicalString(self, digit, n):
        '''
        int digit: the number in the string you would like to count
        int n: which position you would like to count to (inclusive)
        
        Julia's magical string is actually called a Kolakowski sequence!
        
        Compute the sequence up to N places, while keeping track of our digit.
        '''   

        occurences = 0
        
        magical_string = []
        i = 0
        a = 1
        
        while True:
            magical_string.append(a)
            if a == digit: occurences += 1
            if len(magical_string) >= n: return occurences

            if magical_string[i] == 2:
                magical_string.append(a)
                if a == digit: occurences += 1
                if len(magical_string) >= n: return occurences

            a = (a-2)** 2 + 1
            i += 1
            
        
class MagicalStringTest(unittest.TestCase):
    
    def test1(self):
        s = MagicalStringSolution()
        answer = s.MagicalString(1,6)
        expected = 3
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = MagicalStringSolution()
        answer = s.MagicalString(2,4)
        expected = 2
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = MagicalStringSolution()
        answer = s.MagicalString(1,4)
        expected = 2
        self.assertEqual(answer, expected)
        
    def test4(self):
        s = MagicalStringSolution()
        answer = s.MagicalString(2,6)
        expected = 3
        self.assertEqual(answer, expected)

        
if __name__ == '__main__':
    unittest.main()

