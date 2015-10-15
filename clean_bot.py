# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:04:47 2015

@author: breiche

Problem Statement

The goal of Artificial Intelligence is to create a rational agent. 
An agent gets input from the environment through sensors and acts on the 
environment with actuators. In this challenge, you will program a simple bot 
to perform the correct actions based on environmental input. 

Meet the bot MarkZoid. It's a cleaning bot whose sensor is a head mounted 
camera and whose actuators are the wheels beneath it. It's used to clean 
the floor.

The bot here is positioned at the top left corner of a 5*5 grid. Your task 
is to move the bot to clean all the dirty cells.

Input Format

The first line contains two space separated integers which indicate the 
current position of the bot. 
The board is indexed using Matrix Convention 
5 lines follow representing the grid. Each cell in the grid is represented 
by any of the following 3 characters: 'b' (ascii value 98) indicates the 
bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' 
(ascii value 45) indicates a clean cell in the grid. 

Note If the bot is on a dirty cell, the cell will still have 'd' on it. 

Output Format

The output is the action that is taken by the bot in the current step, and 
it can be either one of the movements in 4 directions or cleaning up the cell 
in which it is currently located. The valid output strings are LEFT, RIGHT, 
UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to 
clean the dirty cell. Repeat this process until all the cells on the grid are 
cleaned.

"""

import unittest
import Queue

class CleanBotSolution():
    
    def next_move(self, posr, posc, board):
        '''  
        '''
        bot = (posr, posc)
        dirts = self.GetDirtPositions(board)        
        valid_path = self.BFS(board, bot, dirts)
        
        directions = []
        
        for step in range(1, len(valid_path)):
            prev_step = valid_path[step-1]
            curr_step = valid_path[step]
            d = self.ShoutDirections(prev_step, curr_step)
            directions.append(d)
            
        return "\n".join(directions)
        
    def GetDirtPositions(self, grid):
        '''
        identifies all dirts in the grid.
        '''
        dirt_positions = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'd':
                    dirt_positions.append((r,c))
                    
        return dirt_positions
        
    def BFS(self, graph, start, ends):
        '''
        implements breadth-first-search to find shortest path between start 
        and all possible ends.

        inputs:        
        graph: a matrix 
        start: tuple of (x,y) start position
        end: a list of tuple of (x,y) destinations
        '''
        q = Queue.Queue()

        temp_path = [start]
        q.put(temp_path)
    	
        while q.empty() == False:
            tmp_path = q.get()
            last_node = tmp_path[len(tmp_path)-1]
      
    	    if last_node in ends:
             return tmp_path

            for link_node in self.GetBotNeighbors(graph, last_node):
                if link_node not in tmp_path:
                    new_path = []
                    new_path = tmp_path + [link_node]
                    q.put(new_path)
        
    def GetBotNeighbors(self, grid, position):
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
        shout directions at the bot.
        required output form.
        '''
        curr_x, curr_y= current
        next_x, next_y = nex
        if (curr_x > next_x):
            return "UP"
        elif (curr_x < next_x):
            return "DOWN"
        elif (curr_y < next_y):
            return "RIGHT"
        elif (curr_y > next_y):
            return "LEFT"
        elif (current == nex):
            return "CLEAN"
        

class CleanBotTest(unittest.TestCase):
    
    def ConvertGridToMatrix(self, n, grid):
        '''
        Converts a string into an array of characters of size n x n.
        Used for testing.
        
        grid: grid, represented by a string
        n: numberof rows and columns in a square grid

        returns a tuple with:        
            - the grid as a more usable matrix
        '''
        matrix = [[0 for r in range(n)] for c in range(n)]
        
        string_position = 0
        for r in range(n):
            for c in range(n):                    
                matrix[r][c] = grid[string_position]
                string_position += 1
                
        return matrix 
        
    def setUp(self):
        self.s = CleanBotSolution()
        self.five_matrix = self.ConvertGridToMatrix(5, "b---d-d--d--dd---d------d")
        
    def test_bot_neighbors(self):        
        answer = self.s.GetBotNeighbors(self.five_matrix, (0,0))
        expected = [(0,1), (1,0)]
        self.assertEqual(answer, expected)
        
        answer = self.s.GetBotNeighbors(self.five_matrix, (1,1))
        expected = [(0,1), \
                    (1,0), (1,2), \
                    (2,1)]
        self.assertEqual(answer, expected)
        
        answer = self.s.GetBotNeighbors(self.five_matrix, (2,2))
        expected = [(1,2), \
                    (2,1), (2,3), \
                    (3,2)]
        self.assertEqual(answer, expected) 
        
    def test_integrated(self):
        answer = self.s.next_move(0, 0, self.five_matrix)
        expected0 = "RIGHT"
        expected1 = "DOWN"
        self.assert_((answer == expected0) or (answer == expected1))        


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