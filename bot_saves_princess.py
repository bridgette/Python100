# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:11:41 2015

@author: breiche

Princess Peach is trapped in one of the four corners of a square grid. 
You are in the center of the grid and can move one step at a time in any of 
the four directions. Can you rescue the princess? 

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of 
the grid. This is followed by an NxN grid. Each cell is denoted by '-' 
(ascii value: 45). The bot position is denoted by 'm' and the princess 
position is denoted by 'p'.
Grid is indexed using Matrix Convention.

Output format

Print out the moves you will take to rescue the princess in one go. 
The moves must be separated by '\n', a newline. The valid moves are 
LEFT or RIGHT or UP or DOWN.
"""
import unittest
import Queue

class PrincessSolution():
    
    def displayPathtoPrincess(self, n, grid):
        '''
        Uses breadth-first-search to find a way to princess peach.
        n: number of rows and columns in the square grid
        grid: string representing the contents of every square in the grid       
        '''
        matrix, hero, princess = self.ConvertGridToMatrix(3, grid)
        
        q = Queue.Queue()
        valid_path = self.BFS(matrix, hero, princess, q)
        
        directions = []
        
        for step in range(1, len(valid_path)):
            prev_step = valid_path[step-1]
            curr_step = valid_path[step]
            d = self.ShoutDirections(prev_step, curr_step)
            directions.append(d)
            
        return directions.join(" ")
    
    def ConvertGridToMatrix(self, n, grid):
        '''
        grid: grid, represented by a string
        n: numberof rows and columns in a square grid

        returns a tuple with:        
            - the grid as a more usable matrix
            - the (x,y) position of the hero
            - the (x,y) position of the princess
        '''
        matrix = [[0 for r in range(n)] for c in range(n)]
        hero_pos = ()
        princess_pos = ()
        
        string_position = 0
        for r in range(n):
            for c in range(n):

                if grid[string_position] == 'm':
                    hero_pos = (r,c)
                elif grid[string_position] == 'p':
                    princess_pos = (r,c)
                    
                matrix[r][c] = grid[string_position]
                string_position += 1
                
        return (matrix, hero_pos, princess_pos)
        
    def BFS(self, graph, start, end, q):
        '''
        implements breadth-first-search
        graph: a matrix 
        
        start: tuple of (x,y) hero start position
        end: tuple of (x,y) princess start position
        q: the Queue used for BFS        
        '''
        temp_path = [start]
        q.put(temp_path)
    	
        while q.empty() == False:
            tmp_path = q.get()
            last_node = tmp_path[len(tmp_path)-1]
      
    	    if last_node == end:
             return tmp_path

            for link_node in self.GetHeroMoves(graph, last_node):
                if link_node not in tmp_path:
                    new_path = []
                    new_path = tmp_path + [link_node]
                    q.put(new_path)
        
    def GetHeroMoves(self, grid, position):
        ''' 
        Returns a list of all valid positions the hero can move to on the grid.
        Hero cannot fall off the grid!
        Hero cannot move diagonally!
        '''
        x, y = position        
        neighbors = []
        grid_size = len(grid) # grid is square!
        
        # up
        if (x > 0):
            neighbors.append((x-1, y))
            
        # left
        if (y > 0):
            neighbors.append((x, y - 1))
            
        # right
        if (y + 1 > 0):
            neighbors.append((x, y + 1))
            
        # down
        if (x + 1 < grid_size):
            neighbors.append((x + 1, y))
        
        return neighbors
        
    def ShoutDirections(self, current, nex):
        '''
        shout directions at the hero so he can find his way.
        required output form.
        '''
        curr_x, curr_y= current
        next_x, next_y = nex
        if (curr_x > next_x):
            return "DOWN"
        elif (curr_x < next_x):
            return "UP"
        elif (curr_y < next_y):
            return "LEFT"
        elif (curr_y > next_y):
            return "RIGHT"
        

class MagicalStringTest(unittest.TestCase):
    
    def setUp(self):
        self.s = PrincessSolution()
        self.threeXthree = "p---m-----"
        self.fourXfour = "p---------m-----"
        
    def test_hero_moves(self):
        matrix, _, _ = self.s.ConvertGridToMatrix(3, self.threeXthree)
        
        answer = self.s.GetHeroMoves(matrix, (0,0))
        expected = [(0,1), (1,0)]
        self.assertEqual(answer, expected)
        
        answer = self.s.GetHeroMoves(matrix, (1,1))
        expected = [(0,1), \
                    (1,0), (1,2), \
                    (2,1)]
        self.assertEqual(answer, expected)
        
        answer = self.s.GetHeroMoves(matrix, (2,2))
        expected = [(1,2), (2,1), (2,3)]
        self.assertEqual(answer, expected) 
        
    def integrated_test(self):
        answer = self.s.displayPathtoPrincess(3, self.threeXthree)
        expected0 = "UP LEFT"
        expected1 = "LEFT UP"
        self.assertEqual(answer, expected0) or self.assertEqual(answer, expected1)
        


if __name__ == '__main__':
    unittest.main()

'''# testing from stdin
    m = input()
    
    grid = []
    for i in xrange(0, m):
        grid.append(raw_input().strip())
        
    s = PrincessSolution()
    s.displayPathtoPrincess(m,grid)
'''