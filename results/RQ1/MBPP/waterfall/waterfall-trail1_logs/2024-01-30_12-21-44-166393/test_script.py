def pos_count(numbers: list) -> int:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    positive_count = len([num for num in numbers if num > 0])
    return positive_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pos_count([1, -2, 3, -4]), 2)

if __name__ == '__main__':
    unittest.main()