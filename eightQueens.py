# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5th 2015

@author: breiche
"""
import unittest

class EightQueensSolution(object):
    def eightQueens(self, board):
        '''
        input: board (string with 8 rows x 8 chars)
        Given a chessboard where *s are Queens
        and .s are spaces, return valid if no Queens
        can attack each other and invalid if Queens can 
        attack each other.
        '''
        chess_board = []
        each_row = board.split('\n')
                
        return "valid"
        
        
class EightQueensTest(unittest.TestCase):
    
    def test1(self):
        s = EightQueensSolution()
        answer = s.eightQueens("*.......\
                                ..*.....\
                                ....*...\
                                ......*.\
                                .*......\
                                .......*\
                                .....*..\
                                ...*....")
        expected = "valid"
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = EightQueensSolution()
        answer = s.eightQueens("*.......\
                                ......*.\
                                ....*...\
                                .......*\
                                .*......\
                                ...*....\
                                .....*..\
                                ..*.....")
        expected = "invalid"
        self.assertEqual(answer, expected)
        
        
if __name__ == '__main__':
    unittest.main()

        