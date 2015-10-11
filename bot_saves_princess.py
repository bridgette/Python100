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
        grid: a string representing the contents of every square in the grid       
        '''
        # convert the grid (string) into a more usable matrix
        matrix = [[0 for r in range(n)] for c in range(n)]
        
        string_position = 0
        for r in range(n):
            for c in range(n):
                print grid[string_position], string_position
                matrix[r][c] = grid[string_position]
                string_position += 1
                
        print matrix
        
        # the hero always starts in the center of the grid
        hero = (n/2, n/2)
        print matrix[hero[0]][hero[1]]
        
        q = Queue.Queue()
        
        
        return ""
        
    def BFS(self, graph, start, end, q):
        '''
        implements breadth-first-search
        graph: a matrix 
        
        start: tuple of (x,y) hero start position
        end: tuple of (x,y) princess start position
        q: the Queue used for BFS        
        '''
    	temp_path = [start]
    	
    	q.enqueue(temp_path)
    	
    	while q.IsEmpty() == False:
    		tmp_path = q.dequeue()
    		last_node = tmp_path[len(tmp_path)-1]
    		print tmp_path
      
    		if last_node == end:
    			print "VALID_PATH : ",tmp_path

    		for link_node in neighbors(graph, last_node):
    			if link_node not in tmp_path:
    				new_path = []
    				new_path = tmp_path + [link_node]
    				q.enqueue(new_path)
        
    def neighbors(grid, position):
        ''' 
        returns all valid neighbors of a position on a grid.
        takes into account the edges of the grid
        '''
        return
        

class MagicalStringTest(unittest.TestCase):
    
    def test1(self):
        s = PrincessSolution()
        answer = s.displayPathtoPrincess(3, "p---m-----")
        expected = ""
        self.assertEqual(answer, expected)
        
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