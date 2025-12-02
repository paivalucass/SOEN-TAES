from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = [delimeter] * (len(numbers) - 1)
    result = [item for sublist in zip(numbers, result) for item in sublist]
    result.append(numbers[-1])
    return result

import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_intersperse(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()