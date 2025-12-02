from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove duplicates from a list of integers while preserving the order of the elements. """
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()