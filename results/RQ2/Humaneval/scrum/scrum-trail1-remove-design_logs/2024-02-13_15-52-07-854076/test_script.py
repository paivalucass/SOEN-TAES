from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    :param numbers: List of integers
    :param delimiter: Integer delimiter
    :return: List of integers
    """
    if not numbers:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])
    return result
import unittest

from typing import List


class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_intersperse(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()