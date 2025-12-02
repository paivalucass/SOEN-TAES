from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Invalid input: numbers must be a list of integers")
    
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1:
            result.append(delimiter)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_intersperse_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_intersperse_with_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()