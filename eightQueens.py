# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5th 2015

@author: breiche
"""
import unittest

class EightQueensSolution(object):
    '''
    input: board (string with 8 rows x 8 chars)
    Given a chessboard where *s are Queens
    and .s are spaces, return valid if no Queens
    can attack each other and invalid if Queens can 
    attack each other.
    '''
        
    def eightQueens(self, board):
        '''
        Solves Eight Queens problem by remembering which rows, columns,
        and diagonals upon which we have seen Queens. Runs in O(n^2), where n
        is height/width of chessboard.
        '''
        all_rows = board.split('\n')
        # check basic board configuration 
        if board.count("*") != 8:
            return "invalid"
        if len(all_rows) != 8:
            return "invalid"
            
        columns_seen = {}
        rows_seen = {}
        left_diag_seen = {}
        right_diag_seen = {}
        
        for i, row in enumerate(all_rows):
            for j, square in enumerate(list(row)):
                
                if square == '*':
                    if j in columns_seen:
                        return "invalid"
                    elif i in rows_seen:
                        return "invalid"
                    elif i-j in left_diag_seen:
                        return "invalid"
                    elif i+j in right_diag_seen:
                        return "invalid"
                    else:
                        columns_seen[j] = True
                        rows_seen[i] = True
                        left_diag_seen[i-j] = True
                        right_diag_seen[i+j] = True
                            
        return "valid"
    
        
class EightQueensTest(unittest.TestCase):
    
    def test1(self):
        s = EightQueensSolution()
        answer = s.eightQueens("*.......\n\
..*.....\n\
....*...\n\
......*.\n\
.*......\n\
.......*\n\
.....*..\n\
...*....")
        expected = "invalid"
        self.assertEqual(answer, expected)
        
    def test2(self):
        s = EightQueensSolution()
        answer = s.eightQueens("*.......\n\
......*.\n\
....*...\n\
.......*\n\
.*......\n\
...*....\n\
.....*..\n\
..*....")
        expected = "valid"
        self.assertEqual(answer, expected)
        
    def moreThanEightQueensTest(self):
        s = EightQueensSolution()
        answer = s.eightQueens("*.......\n\
.*....*.\n\
....*...\n\
.......*\n\
.*......\n\
...*....\n\
.....*..\n\
..*....")
        expected = "invalid"
        self.assertEqual(answer, expected)
        
    def moreThanEightRowsTest(self):
        s = EightQueensSolution()
        answer = s.eightQueens("*.......\n\
......*.\n\
....*...\n\
.......*\n\
.*......\n\
...*....\n\
.....*..\n\
..*....\n\
........")
        expected = "invalid"
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()
        