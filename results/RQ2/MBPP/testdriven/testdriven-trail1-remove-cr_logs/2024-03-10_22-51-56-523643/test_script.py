def second_smallest(numbers):
    '''
    Write a function to find the second smallest number in a list.
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    '''
    # Input validation
    if len(numbers) < 2 or len(set(numbers)) < 2:
        return "Input list must contain at least two unique numbers"
    
    # Algorithm implementation
    smallest = min(numbers)
    modified_list = [x for x in numbers if x != smallest]
    second_smallest_number = min(modified_list)
    return second_smallest_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()