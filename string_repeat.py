'''
Determines if a string has all unique letters.
'''

import unittest

class String_Repeat_Solution:
    
    def test_unique(self, s):
        ''' Uses a dictionary to test uniqueness
        of letters in string.
        '''
        d = {}
        for char in s:
            if not str.isalpha(char):
                continue
            if char in d.keys():
                return True
            else:
                d[char] = 1
            
        return False


class Unique_Characters_Test(unittest.TestCase):

    def test_negative(self):
        s = String_Repeat_Solution()
        input_s = "abc defghi jklmnop qrs tuvwxyz!"
        expected = False
        answer = s.test_unique(input_s)
        self.assertEqual(answer, expected)
        
    def test_negative_punc(self):
        s = String_Repeat_Solution()
        input_s = "abc defghi jklmnop qrs tuvwxyz!!!"
        expected = False
        answer = s.test_unique(input_s)
        self.assertEqual(answer, expected)
        
    def test_positive(self):
        s = String_Repeat_Solution()
        input_s = "fizzbuzz"
        expected = True
        answer = s.test_unique(input_s)
        self.assertEqual(answer, expected)   
        
if __name__ == '__main__':
    unittest.main()
