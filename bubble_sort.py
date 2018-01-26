'''
@author:bridgette
1/26/2018
'''
import unittest

class BubbleSortSolution:
    '''
    Keeps track of the number of swaps that happen
    when a list is bubble sorted. For more information, see
    https://en.wikipedia.org/wiki/Bubble_sort
    '''
    def __init__(self):
        self.num_swaps = 0
    
    def bubble_sort(self, array):
        if (array == None):
            return []
        
        for i in range(len(array)):
            for j in range(len(array)-1):
                if (array[j] > array[j + 1]):
                    array[j], array[j + 1] = array[j+1], array[j]
                    self.num_swaps += 1
                    
        return array


class TestBubbleSort(unittest.TestCase):
    def test_empty(self):
        b = BubbleSortSolution()
        answer = b.bubble_sort([])
        expected = []
        self.assertEqual(answer, expected)
        self.assertEqual(b.num_swaps, 0)
    

    def test_sorted(self):
        b = BubbleSortSolution()
        answer = b.bubble_sort([1,2,3])
        expected = [1,2,3]
        self.assertEqual(answer, expected)
        self.assertEqual(b.num_swaps, 0)

    def test_unsorted(self):
        b = BubbleSortSolution()
        answer = b.bubble_sort([3,2,1])
        expected = [1,2,3]
        self.assertEqual(answer, expected)
        self.assertEqual(b.num_swaps, 3)
        
        
if __name__ == '__main__':
    unittest.main()
