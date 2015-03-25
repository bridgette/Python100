# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:08:37 2015

@author: Bridgette
"""
import unittest 

def pig_latin(word):
    ''' 
    Rules of Pig Latin:     Ulesray ofway Igpay Atinlay:
    
    1) The initial consonant cluster is transposed to end of word
    and an -ay is affixed. (Ex. "banana" becomes "anana-bay").
    
    2) For words that begin with vowels, add "way" to the end. 
    (Ex. "image" becomes "imageway").
    
    http://en.wikipedia.org/wiki/Pig_Latin
    '''
    vowels = list("aeiouy")
    
    if word != "" and word[0] in vowels:
        return word + "way"
    
    i=0
    for letter in word:
        if letter in vowels:
            front = word[:i]
            back = word[i:]
            return back + front + "ay"
            
        else: 
            i += 1

    return "Can't be pig latinified."
    
    
class TestPigLatin(unittest.TestCase): 
    
    def test_consonant_starters(self):
        self.assertEqual(pig_latin("pig"), "igpay")
        self.assertEqual(pig_latin("banana"), "ananabay")
        self.assertEqual(pig_latin("trash"), "ashtray")
        self.assertEqual(pig_latin("glove"), "oveglay")
        self.assertEqual(pig_latin("duck"), "uckday")                
    
    def test_vowel_starters(self):
        self.assertEqual(pig_latin("egg"), "eggway")
        self.assertEqual(pig_latin("inbox"), "inboxway")
        self.assertEqual(pig_latin("eight"), "eightway")
    
    def test_undefined_words(self):
        self.assertEqual(pig_latin(""), "Can't be pig latinified.")
        self.assertEqual(pig_latin("zzzzzzz"), "Can't be pig latinified.")
        self.assertEqual(pig_latin("$%^&*("), "Can't be pig latinified.")

        
if __name__ == '__main__':
    unittest.main()