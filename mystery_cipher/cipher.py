# -*- coding: utf-8 -*-
"""
Cipher

Translate the mystery string.
"""
import unittest
from english_scorer import ScoreEnglish

class CaesarCipher:
    '''
    Caesar Cipher is a substitution cipher in which each letter in the 
    plaintext is replaced by a letter some fixed number of positions 
    down the alphabet.
    https://en.wikipedia.org/wiki/Caesar_cipher
    '''
    def __init__(self, offset):
        self.offset = offset
        
    def decrypt_string(self, encoded_string):
        '''
        Caesar Cipher an entire string.
        '''
        cipher = list()
        for c in encoded_string:
            
            if c.isalpha():
                cipher.append(self.decrypt_chr(c))
                
            else:
                cipher.append(c)

        return ''.join(cipher)
        
    def decrypt_chr(self, char):
        '''
        Cipher each char.
        '''
        is_upper_case = char.isupper()

        if is_upper_case:
            orig_ord = ord('A')
            end_ord  = ord('Z')
        else:
            orig_ord = ord('a')
            end_ord  = ord('z')

        temp_ord = ord(char)+self.offset
        offset_ord = (temp_ord - end_ord - 1) % 26
        return chr(orig_ord + offset_ord)


class TestCaesarCiper(unittest.TestCase):
    def setUp(self):
        self.c = CaesarCipher(3)
        
    def testWord(self):
        answer = self.c.decrypt_string("QEB")
        expected = "THE"
        self.assertEqual(answer, expected)
        
    def testPhrase(self):
        answer = self.c.decrypt_string("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")
        expected = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
        self.assertEqual(answer, expected)
        
    def handlePunct(self):
        answer = self.c.decrypt_string("Ebiil...")
        expected = "Hello..."
        self.assertEqual(answer, expected)
    
    def handleEmpty(self):
        answer = self.c.decrypt_string("")
        expected = ""
        self.assertEqual(answer, expected)



if __name__ == '__main__':
    #unittest.main()    
    mystery_string = "XDDFOIZWMJ ZODFOI ZWSDWSON TYDF WLZWERZO ER FTERLHON? SDTY'DO ER ZWDFTY DFWE WEOIIU, XDON WLRMDFLHSDDOON. OIDOON ERNMERZWDFIU WEDFRM TYOON ERIUDOXDONROM. FTDFDFMJ ZWOIRTWS."
    scorer = ScoreEnglish()
    scored_decryptions_map = {}
        
    # is it a Caesar Cipher?
    for possible_offset in range(27):
        
        # decrypt
        caesar = CaesarCipher(possible_offset)
        decoded_string = caesar.decrypt_string(mystery_string)
        
        # score 
        score = scorer.score_English(decoded_string)
        scored_decryptions_map[decoded_string] = score
        
    # print top 5 Caesar cipher guesses
    for a, b in sorted(scored_decryptions_map.iteritems(), key=lambda item: item[1], reverse=True)[:5]:
        print a, b
        
    # is it a general substitution cipher?