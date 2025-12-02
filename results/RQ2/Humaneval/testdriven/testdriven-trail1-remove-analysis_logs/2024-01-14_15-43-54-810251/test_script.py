from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimiter)
        result.append(num)

    return result
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_non_empty_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()