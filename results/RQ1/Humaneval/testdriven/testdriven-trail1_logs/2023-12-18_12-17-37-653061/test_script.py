from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not all(isinstance(num, int) for num in numbers) or not isinstance(delimiter, int):
        raise ValueError("Input validation error: 'numbers' must be a list of integers and 'delimiter' must be an integer")
    
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1:
            result.append(delimiter)
    return result
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_non_empty_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()