# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 10:12:49 2016

@author: breiche
"""
import unittest

class ScoreEnglish(object):

    def __init__(self):
        self.english_words = self.import_english_dict()        
        
    def score_English(self, s):
        ''' 
        returns the count of how many valid English words are in the string s.
        A high count indicates that the decryption was likely successful.
        '''
        s = s.lower()
        words_in_string = s.split(" ")
        intersection = list(set(self.english_words) & set(words_in_string))
        return len(intersection)
    
    def import_english_dict(self, pathname = "english.txt"):
        '''
        Imports an english dictionary, where every word is on a new line.
        '''
        print "Importing a list of english words at ", pathname
        valid_words = []
        try:
            f = open(pathname, 'r')
            for line in f:
                valid_words.append(line.strip())
            print "Successfully imported", len(valid_words), "from", pathname
        
        except IOError:
            print "Error while opening file. I don't think it exists."
        
        return valid_words
        

class TestEnglishScorer(unittest.TestCase):
    def setUp(self):
        self.s = ScoreEnglish()
        
    def testWord(self):
        answer = self.s.score_English("This is an excellent English sentence!")
        expected = 4
        self.assertEqual(answer, expected)
        
    def testNonEnglish(self):
        answer = self.s.score_English("Yoooa dfd dkddkfjdieqm dndf")
        expected = 0
        self.assertEqual(answer, expected)
        
    def handlePunct(self):
        answer = self.s.score_English("Writhing!")
        expected = 1
        self.assertEqual(answer, expected)
    
    def handleEmpty(self):
        answer = self.s.score_English("")
        expected = 0
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()   
    