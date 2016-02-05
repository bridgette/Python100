# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 10:12:34 2016

@author: breiche
"""
import unittest

class SubstitutionCipher(object):
    '''
    A general substitution cipher, where every letter can match to any other
    letter.
    
    Can accept guesses, a map with key = encoded char; value = decoded char.
    '''
    def __init__(self, guesses = {}, encoded_string = ""):
        self.guesses = guesses
        self.encoded_string = encoded_string
        self.decoded_string = ""
        
    def decrypt_string(self):
        '''
        '''
        for guess in self.guesses:
            continue

        return
        
    def apply_guesses(self):
        '''
        '''
        return
        
    def decrypt_chr(self, char):
        return


class TestSubstitutionCiper(unittest.TestCase):
    def setUp(self):
        self.s = SubstitutionCipher()
        
    def testWord(self):
        answer = ""
        expected = ""
        self.assertEqual(answer, expected)
        
    def testPhrase(self):
        answer = ""
        expected = ""
        self.assertEqual(answer, expected)
        
    def handlePunct(self):
        answer = ""
        expected = ""
        self.assertEqual(answer, expected)
    
    def handleEmpty(self):
        answer = ""
        expected = ""
        self.assertEqual(answer, expected)
        
        
if __name__ == '__main__':
    unittest.main()   