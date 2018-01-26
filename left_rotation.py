# -*- coding: utf-8 -*-
"""
@author: bridgette
"""
import unittest

class RotationSolution:
    '''
    Given an array with length n and an int d,
    rotate each item in the array to the left d spaces.
    '''
        
    def left_rotation(self, array, d):
        '''
        Calculate new index of element in array.
        Requires O(n) space/time.
        '''
        n = len(array)
        if n == 0 or d == 0:
            return array

        rotated_array = [None] * n

        for i, element in enumerate(array):
            new_index = (i - d) % n
            rotated_array[new_index] = element
        
        return rotated_array 
        
                    
class Test_Rotation(unittest.TestCase):

    def test_rotation(self):
        s = RotationSolution()
        self.assertEqual( s.left_rotation([1, 2, 3, 4, 5], 1), [2, 3, 4, 5, 1] )
        self.assertEqual( s.left_rotation([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2] )
        self.assertEqual( s.left_rotation([1, 2, 3, 4, 5], 3), [4, 5, 1, 2, 3] )
        self.assertEqual( s.left_rotation([1, 2, 3, 4, 5], 4), [5, 1, 2, 3, 4] )

    def test_rotation_nulls(self):
        s = RotationSolution();
        self.assertEqual( s.left_rotation([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5] )
        self.assertEqual( s.left_rotation([], 4), [] )

        
if __name__ == '__main__':
    unittest.main()
        
