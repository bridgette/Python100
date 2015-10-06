# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 14:28:29 2015

@author: breiche

You are part of a team developing software to help students learn basic mathematics. 
You are to write one part of that software, which is to display possibly improper 
fractions as mixed fractions. A proper fraction is one where the numerator is 
less than the denominator; a mixed fraction is a whole number followed by a 
proper fraction. For example the improper fraction 27/12 is equivalent to the 
mixed fraction 2 3/12. You should not reduce the fraction (i.e. don’t 
change 3/12 to 1/4).
"""

import unittest

class MixedFractionsSolution(object):
    def mixedFractions(self, fractionAsString):
        '''
        input: a string with two integers, seperated by a space
        output: string displaying mixed fraction as a whole number, space, 
            followed by a proper fraction
        '''
        numerator, denominator = fractionAsString.split(" ")
        
        numerator = int(numerator)
        denominator = int(denominator)
        
        wholenum = 0
        remainder = 0
        
        if numerator >= denominator:
            wholenum = numerator / denominator
        remainder = numerator % denominator
            
        return "{0} {1}/{2}".format(str(wholenum), str(remainder), str(denominator))
        
        
class MixedFractionsTest(unittest.TestCase):
    
    def test1(self):
        s = MixedFractionsSolution()
        answer = s.mixedFractions("27 12")
        expected = "2 3/12"
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = MixedFractionsSolution()
        answer = s.mixedFractions("2460000 98400")
        expected = "25 0/98400"
        self.assertEqual(answer, expected)
        
    def test3(self):
        s = MixedFractionsSolution()
        answer = s.mixedFractions("3 4000")
        expected = "0 3/4000"
        self.assertEqual(answer, expected)
        
        
if __name__ == '__main__':
    unittest.main()

        