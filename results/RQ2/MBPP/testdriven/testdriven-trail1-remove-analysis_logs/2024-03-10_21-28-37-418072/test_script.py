def second_smallest(numbers):
    '''Write a function to find the second smallest number in a list.'''
    if len(numbers) < 2:
        return "Error: List should have at least 2 elements"
    smallest_num = float('inf')
    second_smallest_num = float('inf')
    for num in numbers:
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
        elif num < second_smallest_num and num != smallest_num:
            second_smallest_num = num
    if second_smallest_num == float('inf'):
        return "Error: All numbers in the list are same"
    return second_smallest_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()