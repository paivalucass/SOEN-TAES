from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])

    return result
import unittest

class Test(unittest.TestCase):
    def test_intersperse(self):
        self.assertEqual(intersperse([], 4), [])
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()